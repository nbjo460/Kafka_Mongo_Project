import os
import json
import parameters as params
from pymongo import MongoClient

def connection(func):
    """
    Decorator function.
    Allow to open and close connection each func, with try except.
   """
    def wrapper(dal, *args, **kwargs):
        client = None
        try:
            client = MongoClient(dal.URI)
            client.admin.command("ping")
            print("Connected successfully")
            db = client[dal.DBNAME]
            result = func(dal, db,*args, **kwargs)
            return result
        except Exception as e:
            print(f"Exception: {e}")
        finally:
            try:
                client.close()
                print("closed")
            except Exception as e:
                print("Can't close ", e)

    return wrapper

class Dal:
    """
    Object that make connection with mongodb server, and get data.
    """
    def __init__(self):
        self.USER = params.MONGO_USER
        self.PASSWORD = params.MONGO_PASSWORD
        self.HOST = params.MONGO_HOST
        self.PORT = params.MONGO_PORT
        self.TOPIC = params.KAFKA_TOPIC

        self.URI = params.MONGO_URI
        self.DBNAME = params.MONGO_DBNAME




    # @connection
    # def get_all_messages_interesting(self, db):
    #     """
    #     Returns all the messages of interesting.
    #     :return: json
    #     """
    #     print("Fetching messages.")
    #     collection = db[params.INTERESTING_COLLECTION]
    #     messages = list(collection.find({}, {"_id":0}))
    #     print(f"{len(messages)} messages loaded.")
    #     return messages
    #
    # @connection
    # def get_all_messages_not_interesting(self, db):
    #     """
    #             Returns all the messages of not interesting.
    #             :return: json
    #             """
    #     print("Fetching messages.")
    #     collection = db[params.NOT_INTERESTING_COLLECTION]
    #     messages = list(collection.find({},{"_id":0}))
    #     print(f"{len(messages)} messages loaded.")
    #     return messages

    #
    # @connection
    # def send_interesting(self,db, message):
    #     collection = db[params.INTERESTING_COLLECTION]
    #     collection.insert_one(message)
    #
    # @connection
    # def send_not_interesting(self, db, message):
    #     collection = db[params.NOT_INTERESTING_COLLECTION]
    #     collection.insert_one(message)

    @connection
    def get_all_messages(self, db):
        """
        Returns all the messages from topic.
        :return: json
        """
        print("Fetching messages.")
        collection = db[self.TOPIC]
        messages = list(collection.find({}, {"_id":0}))
        print(f"{len(messages)} messages loaded.")
        return messages

    @connection
    def send_message(self, db, message):
        db[self.TOPIC].insert_one(message)

