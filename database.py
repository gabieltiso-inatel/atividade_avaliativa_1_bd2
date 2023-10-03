import os
import pymongo
from dotenv import load_dotenv

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            load_dotenv()
            connectionString = os.getenv("MONGODB_ATLAS_CONN_STR")
            
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
        except Exception as e:
            print(e)

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
