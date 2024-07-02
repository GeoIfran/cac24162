#Importo librerias necesarias segun el dicatado del curso
import os
import mysql.connector
from flask import g, __init__
from dotenv import load_dotenv
#Cargamos las variables de entorno del achivo .env
load_dotenv()
#Comfiguro los datos para el uso de la base de datos segun las variables traidas de .env
DATABASE_CONFIG={
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 3306)
}
# Función para obtener la conexión a la base de datos
def get_db():
# Si 'db' no está en el contexto global de Flask 'g'
    if 'db' not in g:
    # Crear una nueva conexión a la base de datos y guardarla en 'g'
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
        print('Esta es la respuesta al conectar a la base de datos',g.db)
    # Retornar la conexión a la base de datos
    return g.db
# Función para cerrar la conexión a la base de datos
def close_db(e=None):
# Extraer la conexión a la base de datos de 'g' y eliminarla
    db = g.pop('db', None)
# Si la conexión existe, cerrarla
    if db is not None:
        db.close()
# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
# Registrar 'close_db' para que se ejecute al final del contexto de la aplicación
    app.teardown_appcontext(close_db)
    print(app.teardown_appcontext(close_db))