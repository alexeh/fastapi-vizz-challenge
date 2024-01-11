import pymongo
import boto3




def get_mongo_client():
    client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
    db = client["local"]
    collection = db["emissions"]
    return collection


def get_dynamodb_client():
    client = boto3.resource('dynamodb', region_name='eu-west-3').Table('emissions')
    return client