import pymongo
import boto3

from config.config import get_settings

settings = get_settings()
aws_access_key_id = settings.AWS_ACCESS_KEY
aws_secret_access_key = settings.AWS_SECRET_KEY



def get_mongo_client():
    client = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
    db = client["local"]
    collection = db["emissions"]
    return collection


def get_dynamodb_client():
    client = boto3.resource('dynamodb', region_name='eu-west-3', aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key).Table('emissions')
    return client