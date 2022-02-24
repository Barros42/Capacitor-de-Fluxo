from pymongo import MongoClient

from Shared.Framework.Configurations.__main__ import CONFIG_DATABASE_NAME, CONFIG_DATABASE_CONNECTION_STRING

def getDatabase():
    return MongoClient(CONFIG_DATABASE_CONNECTION_STRING)[CONFIG_DATABASE_NAME]
    pass
