from collections import OrderedDict
from pymongo import MongoClient

class DbConnection:
    def __init__(self):
        self.mongo = MongoClient('mongodb://admin:codespider@localhost:27017/')
        self.db = self.mongo.quasardb

    def connection_start(self):
        return self.db

    
    def connection_quasar_start(self):
        schema = {
            "$jsonSchema":{
                "bsonType": "object",
                "additionalProperties": False,
                "properties":{
                    "_id":{
                        "bsonType":"objectId"
                    },
                    "timestamp":{
                        "bsonType":"date",
                    },
                    "transactionId":{"type":"string","minLength":1},
                    "bankName":{"type":"string","minLength":1},
                    "fileName":{"type":"string","minLength":1},
                    "password":{"type":"string"}
                }
            }
        }
        try:
            if "quasar" in self.db.list_collection_names():
                query = [('collMod','quasar'),
                         ('validator',schema),
                         ('validationLevel','moderate')
                        ]
                query = OrderedDict(query)
                self.db.command(query)

            else:
                self.db.create_collection("quasar", validator = schema)
        except Exception as e:
            print (e)
        return self.db

    def connection_close(self):
        self.mongo.close()
        return True