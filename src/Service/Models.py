from Service import DbConnection
import datetime
import json

class Models:
    def __init__(self):
        self.db_connection = DbConnection.DbConnection()

    def save_verification_input(self, verificationInput):
        timestamp = datetime.datetime.utcnow()
        response = {}
        db = self.db_connection.connection_quasar_start()
        if "quasar" in db.list_collection_names():
            collections = db.quasar
        else:
            db.create_collection("quasar")
            collections = db.quasar
        try:
            [response for response in collections.find({'transactionId': verificationInput["transactionId"]})]
            if len(response) == 0:
                insertResponse = collections.insert_one({verificationInput})
            else:
                return "User already exisit"

        except Exception as e:
            print (e)
            return e
        finally:
            self.db_connection.connection_close()

