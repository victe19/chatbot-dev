import json
from asyncio.log import logger
import collections
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# cred = credentials.Certificate("db/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

"""WRITE DATA"""

# # Create a collection
# db.collection('people').add({'name':'Blai', 'age':42})

# # Add data
# data = {
#     u'name': u'Los Angeles',
#     u'state': u'CA',
#     u'country': u'USA'
# }

# # Add a new doc in collection 'cities' with ID 'LA'
# db.collection(u'cities').document(u'LA').set(data)


"""READ DATA"""

# 1 -- Know id
# result = db.collection('cities').document('LA').get()
# if result.exists:
#     print(result.to_dict())
# else:
#     print("Doesn't exist")

# # 2 -- Get all documents in a collection
# docs = db.collection('cities').get()
# for doc in docs:
#     print(doc.to_dict())

# 3 - SQLQuerying
docs = db.collection('cities').where("name", "==", "Barcelona" ).get() # array_contains, in --> as operators
for doc in docs:
    print(doc.to_dict())

def get_from_db(colection: str, row) -> dict:
    
    data_dict = db.collection(colection).document(row).get()
    if data_dict.exists:
        return data_dict.to_dict()
    else: 
        logger.error(f"Information not found in db")


db.collection('people').add({'name':'Blai', 'age':42})

# Add data
data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection(u'cities').document(u'LA').set(data)


def post_to_db(filename: str, collection_name: str, document_name: str):

    with open(filename) as json_file:
        data = json.load(json_file)
    
    db.collection(collection_name).document(document_name).set(data)

    