import os
from pymongo import MongoClient

# MONGODB_URL = "mongodb://seu_usuario:senha@seu_servidor_mongodb:porta"
MONGODB_URL = "mongodb://mongouser:mongopassword@mongodb:27017/"

mongo_client = MongoClient(MONGODB_URL)

def get_mongo_db():
    db = mongo_client.raizen_weather_db
    return db
