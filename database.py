from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def insert_college(data):
    collection.insert_one(data)

def get_colleges():
    return list(collection.find({}, {"_id": 0}))