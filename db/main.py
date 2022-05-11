import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("db/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Create a collection
db.collection('people').add({'name':'Blai', 'age':42})

# Add data
data = {
    u'name': u'Los Angeles',
    u'state': u'CA',
    u'country': u'USA'
}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection(u'cities').document(u'LA').set(data)