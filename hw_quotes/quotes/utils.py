from pymongo import MongoClient


def get_mongo_db():
    client = MongoClient("mongodb://localhost")

    db = client.hw
    return db
