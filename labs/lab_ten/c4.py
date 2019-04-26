import pprint

from bson.objectid import ObjectId
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    
    db = client["mongo_db_lab"]
    
    collection = db.definitions
    
    print("All records:")
    pprint.pprint(collection.find())
    
    print("One record:")
    pprint.pprint(collection.find_one())

    print("Specific record:")
    pprint.pprint(collection.find_one({"word": "Ack"}))

    print("Record by object id:")
    pprint.pprint(collection.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8b8")}))

    print("Insert object:")
    collection.insert_one({"word": "Khalidius Maximus", "definition":"I was running Down the boulevard"})

    pprint.pprint(collection.find_one({"word": "Khalidius Maximus"}))