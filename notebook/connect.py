from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI_ATLAS = os.getenv("MongoDB_URI_Atlas")
DATABASE_NAME=os.getenv("MongoDB_Data")

try:
    client = MongoClient(MONGO_URI_ATLAS)
    print("Conectado a Atlas correctamente")
    db = client[DATABASE_NAME]
    colecciones = db.list_collection_names()
    print("Conectado Atlas, Base de datos", (DATABASE_NAME))
    print("Colecciones: ", (colecciones))

except errors.ServerSelectionTimeoutError as e:
    print("No se pudo conectar al servidor")

except errors.OperationFailure as e:
    print("Error de Autenticacion o permisos: ", e)
