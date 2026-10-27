import os, re ,emoji, pymongo

from atproto import Client
from dotenv import load_dotenv
from google import genai


# Función para obtener el feed completo de un usuario de Bluesky

def obtener_feed(client, actor, limit):

    feed = client.get_author_feed(actor= actor, limit= limit)

    return feed


# Función para limpiar los datos que hemos obtenido del feed

def limpiar_feed(client):

    data = obtener_feed(client, "did:plc:2u4l5fk7rthgo5oprwe46rxj", 30)

    feed_final = []

    for f in data.feed:

        feed = f.post.record.text

        feed_limpio = emoji.replace_emoji(feed, replace='')

        feed_limpio = re.sub(r'https?://\S+|www\.\S+', '', feed_limpio)

        feed_final.append({"texto": feed_limpio})

    return feed_final


# Función para almacenar el feed completo en mongodb

def almacenar_en_mongodb(client, data):

    try:

        db = client["bluesky"]
        collection = db["feed"]

        result = collection.insert_many(data)

        print("Se ha creado la base de datos correctamente")

    except Exception as e:
        print(f"Ha ocurrido un error de tipo: {e}")



# Creamos el cliente con las variables de entorno de Bluesky

load_dotenv()

BSKY_IDENTIFIER = os.environ.get('BSKY_IDENTIFIER')
BSKY_PASSWORD = os.environ.get('BSKY_PASSWORD')

client = Client()

client.login(BSKY_IDENTIFIER, BSKY_PASSWORD)

feed_limpio = limpiar_feed(client)


# Creamos el cliente de mongodb para gestionar el proceso de guardar el feed

client_mongo = pymongo.MongoClient("mongodb://root:contra@localhost:27017/")

databases_list = client_mongo.list_database_names()

# Comprobamos que la base de datos no esté repetida

if "bluesky" not in databases_list:
    
    almacenar_en_mongodb(client_mongo, feed_limpio)


# Creamos el cliente de gemini para utilizar la API

CLAVE_API_GEMINI = os.environ.get('CLAVE_API_GEMINI')
client_gemini = genai.Client(api_key=CLAVE_API_GEMINI)

# Creamos la cadena de caracteres con todo el feed para usarlo en el prompt

textos_sueltos = [texto["texto"] for texto in feed_limpio]

feed_gemini = " ".join(textos_sueltos)

prompt = f"Te voy a pasar el feed de un usuario, quiero que lo analices y me expliques en que consiste el feed de este usuario. {feed_gemini} Además, quiero que me respondas únicamente con el resumen del perfil."


# Hacemos la consulta a la API de gemini, eligiendo el modelo y pasando el prompt

response = client_gemini.models.generate_content(
    model = "gemini-3.5-flash",
    contents = prompt
)


# Almacenamos el texto de la respuesta de gemini y lo guardamos en un .txt

respuesta = response.text or "El modelo no generó ninguna respuesta"

with open("1_3_Lopez_Pina_Antonio.txt", "w", encoding="utf-8") as archivo:
    archivo.write(respuesta)


# Almacenamos la respuesta de gemini, junto al feed analizado, y el código del perfil. En vez de insertar el documento, lo vamos a actualizar para que no haya duplicados en el caso de que se ejecute varias veces el código

db = client_mongo["bluesky"]

documento_analisis = {
    "perfil": "did:plc:2u4l5fk7rthgo5oprwe46rxj",
    "resumen_gemini": respuesta,
    "feed_analizado": feed_limpio 
}

filtro = {"perfil": "did:plc:2u4l5fk7rthgo5oprwe46rxj"}
nuevos_datos = {"$set": documento_analisis}

db["analisis_perfiles"].update_one(filtro, nuevos_datos, upsert=True)