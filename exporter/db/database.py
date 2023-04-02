import pymongo


def get_mongo_client():
    client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
    db = client["local"]
    collection = db["emissions"]
    return collection
