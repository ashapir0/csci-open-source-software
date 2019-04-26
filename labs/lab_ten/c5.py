import random
import datetime

from pymongo import MongoClient

def get_random_word(client):
    db = client["mongo_db_lab"]
    collection = db.definitions
    
    words = list(collection.find())
    n = random.randint(0, len(list(words)))
    
    collection.update_one({"word": words[n]["word"]}, {"$push": {"dates": datetime.datetime.now()}})
    return words[n]["word"], words[n]["definition"]

if __name__ == "__main__":
    client = MongoClient()
    print(get_random_word(client))
