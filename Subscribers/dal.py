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
            print("opened")
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
        self.USER = os.getenv("USER", "root")
        self.PASSWORD = os.getenv("PASSWORD", "menachemYarhi")
        self.HOST = os.getenv("HOST")
        self.PORT = os.getenv("PORT", 27017)

        self.URI = os.getenv("URI", f"mongodb://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}")
        self.DBNAME = os.getenv("DBNAME", "IranMalDB")




    @connection
    def get_all_messages_interesting(self, db):
        """
        Returns all the messages of interesting.
        :return: json
        """
        print("Fetching messages.")
        collection = db[params.INTERESTING_COLLECTION]
        messages = list(collection.find())
        print(f"{len(messages)} messages loaded.")
        return messages

    @connection
    def get_all_messages_not_interesting(self, db):
        """
                Returns all the messages of not interesting.
                :return: json
                """
        print("Fetching messages.")
        collection = db[params.NOT_INTERESTING_COLLECTION]
        messages = list(collection.find())
        print(f"{len(messages)} messages loaded.")
        return messages


    @connection
    def send_interesting(self,db, message):
        collection = db[params.INTERESTING_COLLECTION]
        collection.insert_one(message)

    @connection
    def send_not_interesting(self, db, message):
        collection = db[params.NOT_INTERESTING_COLLECTION]
        collection.insert_one(message)


