import os
import json
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
        self.URI = os.getenv("HOST", "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
        self.USER = os.getenv("USER", "IRGC")
        self.DBNAME = os.getenv("DBNAME", "IranMalDB")
        self.PASSWORD = os.getenv("PASSWORD", "iraniraniran")

        self.INTERESTING_COLLECTION = "Interesting"
        self.NOT_INTERESTING_COLLECTION = "NotInteresting"


    @connection
    def get_tweets(self, db):
        """
        Ruturns list of all tweets.
        :return: list
        """
        print("Fetching tweets.")
        tweets = list(collection.find())
        print(f"{len(tweets)} tweets loaded.")
        return tweets

    @connection
    def send_interesting(self,db, message):
        collection = db[self.INTERESTING_COLLECTION]

    @connection
    def send_not_interesting(self, db, message):
        collection = db[self.NOT_INTERESTING_COLLECTION]


