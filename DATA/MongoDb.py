from pymongo import MongoClient

def get_database():
# Database connection
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
# Create database
    return client['Synthetic-Healthcare']

#  Create collections
db_name = get_database()
collection_name = db_name['patient_condition']

# insert data
def insert_db(db):
    collection_name.insert_many(db)

def delete_all_db_value():
    for value in collection_name.find():
        collection_name.delete_one(value)









