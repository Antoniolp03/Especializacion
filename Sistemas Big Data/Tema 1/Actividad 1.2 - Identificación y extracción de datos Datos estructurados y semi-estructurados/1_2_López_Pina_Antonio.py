import requests
import pandas as pd
import pymongo
from datetime import datetime, timezone

def hacer_peticion():
    r = requests.get('https://servicios.ine.es/wstempus/jsCache/ES/DATOS_TABLA/25171')
    return r.json()

def crear_base_de_datos(client, data_json):

    try:

        db = client["ine_database"]
        collection = db["ipv_raw"]

        result = collection.insert_many(data_json)

        print("Se ha creado la base de datos correctamente")

    except:
        print("Ha ocurrido un error al crear la base de datos")


def crear_dataframe(data_json):

    try:

        data = []
        mapa_periodo = {19: 1, 20: 2, 21:3, 22:4}
        
        for serie in data_json:

            nombre = serie.get('Nombre')

            if "Índice" not in nombre:
                continue

            if "Vivienda nueva" in nombre or "Vivienda segunda mano" in nombre:
                continue

            for registro in serie.get('Data', []):

                data.append({
                    'Lugar': nombre,
                    'Año': registro.get('Anyo'),
                    'Periodo': mapa_periodo[registro.get('FK_Periodo')],
                    'IPV': registro.get('Valor')
                })

        df = pd.DataFrame(data)

        df['Lugar'] = df['Lugar'].astype(str)
        df['Año'] = df['Año'].astype(int)
        df['Periodo'] = df['Periodo'].astype(int)
        df['IPV'] = df['IPV'].astype(float)

        return df

    except:
        print("Ha ocurrido un error al crear el dataframe")


client = pymongo.MongoClient("mongodb://root:contra@localhost:27017/")

databases_list = client.list_database_names()

if "ine_database" not in databases_list:
    
    crear_base_de_datos(client, hacer_peticion())

df = crear_dataframe(hacer_peticion())

time_unix = datetime.now(timezone.utc).timestamp()

# Para craer el csv pongo sep=';', decimal=',' para que Pandas use ; para separar las columnas y la , para los decimales, ya que sino Excel lee mal los datos y le quita el . de los decimales al IPV 
df.to_csv(f"IPV_{time_unix}.csv", index=False, sep=';', decimal=',')