from pymongo import MongoClient
import certifi

MONGO_URI="mongodb+srv://dstevengmz1293:I47p1xVezRj7vGWw@cluster0.6jt6j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

ca=certifi.where()

def dbconexion():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db=client["db_productos_app"]
    except ConnectionError:
        print("Error de conexion con base de datos")
    return db
