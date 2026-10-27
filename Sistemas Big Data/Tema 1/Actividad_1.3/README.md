📊 Analizador de Perfiles (Bluesky + IA Gemini)

Un pipeline de datos en Python que extrae publicaciones de la red social Bluesky, procesa los textos no estructurados para limpiarlos, los guarda en MongoDB y genera un resumen automático del perfil del usuario utilizando la Inteligencia Artificial de Google Gemini (modelo 3.5 Flash).

🚀 Características Principales (Features)

Extracción de datos: Conexión al SDK de Bluesky para descargar el timeline de un usuario.

Procesamiento de texto: Limpieza automática de ruido (eliminación de URLs y emojis) para optimizar el análisis de la IA.

Base de Datos NoSQL: Guardado de los datos preprocesados en MongoDB para evitar descargar la misma información constantemente.

Análisis con LLMs: Construcción de un prompt dinámico que inyecta los posts en la API de Google Gemini para obtener un resumen temático del perfil.

🛠️ Tecnologías Utilizadas

Lenguaje: Python (gestionado con uv)

Librerías: atproto (Bluesky), google-genai (IA), pymongo (Bases de datos), python-dotenv (Seguridad), emoji y re.

Infraestructura: MongoDB local.

📋 Requisitos Previos

Python 3 y el gestor de paquetes uv instalados en tu sistema.

MongoDB Server ejecutándose en tu equipo local (localhost:27017).

Claves de acceso para la API de Gemini y cuenta de Bluesky.

⚙️ Instalación y Configuración

Clonar repositorio e instalar dependencias con uv:

git clone <URL_DEL_REPOSITORIO>
cd <CARPETA>

uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt


Configurar credenciales (.env):
Crea un archivo .env en la carpeta principal. Asegúrate de que este archivo está incluido en tu .gitignore para no filtrar tus contraseñas.

BSKY_IDENTIFIER=tu_usuario
BSKY_PASSWORD=tu_app_password
CLAVE_API_GEMINI=tu_api_key


💻 Guía de Uso

Ejecuta el archivo principal para iniciar el proceso completo (Extracción -> Limpieza -> Base de datos -> IA). Gracias a uv, puedes ejecutarlo directamente así:

uv run main.py


El script mostrará un mensaje de éxito al conectarse a la base de datos y, tras unos segundos, imprimirá en la consola la respuesta elaborada por Gemini.

🧪 Pruebas (Testing)

Para probar que el flujo de datos es correcto, revisa tu cliente de base de datos (ej. MongoDB Compass) tras la ejecución. Deberías ver una nueva base de datos llamada bluesky con una colección feed que contiene los textos ya limpios, sin emojis ni enlaces web.

📁 Estructura del Proyecto

main.py: Contiene toda la lógica de conexión, extracción y llamada a la API.

requirements.txt: Listado de dependencias para uv pip.

.env: Archivo local de variables de entorno.

.gitignore: Archivos excluidos del control de versiones.

🤝 Cómo Contribuir (Contributing)

Las sugerencias y mejoras son bienvenidas. Si tienes alguna idea para optimizar los prompts o mejorar el proceso de limpieza de datos, puedes abrir una Issue o enviar un Pull Request.

✍️ Autores y Agradecimientos

Proyecto desarrollado por Antonio López Pina. Agradecimientos a la documentación oficial de atproto y Google AI Studio.

📄 Licencia

Este proyecto utiliza la licencia MIT License. Eres libre de usarlo, modificarlo y distribuirlo.