from pymongo import MongoClient

class Mongo():

    def __init(self):
        client = MongoClient('localhost', 27017)
        self.db = client.db
        #self.collection = client.db.collection


    def getDataBase(self):
        return

    def getCollection(self):
        return self.db.collection_names()

    def insertToCollection(self, dict):
        self.db.collection.insert(dict)


mongo = Mongo()
mongo.insertToCollection({"item": 1})
