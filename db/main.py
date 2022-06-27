import json
from asyncio.log import logger
import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore

# cred = credentials.Certificate("db/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()


def get_from_db(colection: str, row) -> dict:
    
    data_dict = db.collection(colection).document(row).get()
    if data_dict.exists:
        return data_dict.to_dict()
    else: 
        logger.error(f"Information not found in db")


def post_to_db(filename: str, collection_name: str, document_name: str):

    with open(filename) as json_file:
        data = json.load(json_file)
    
    db.collection(collection_name).document(document_name).set(data)

    