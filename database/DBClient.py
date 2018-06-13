from pymongo import MongoClient
from pymongo.son_manipulator import SONManipulator

import sys
sys.path.insert(0, sys.path[0] + "/..")
from config import app_config as cfg

class DBClient():

    class __ObjectIdManipulator(SONManipulator):
        def transform_outgoing(self, son, collection):
            son[u'_id'] = str(son[u'_id'])
            return son

    __instance = None

    def __init__(self, collectionName):
        mongoUrl = cfg.db_uri
        self.dbName = "contactbook"

        if DBClient.__instance is None:
            DBClient.__instance = MongoClient(mongoUrl)

        self.__collectionName = collectionName

    def getCollectionInstance(self):
        db = self.__instance[self.dbName]
        db.add_son_manipulator(self.__ObjectIdManipulator())
        return db[self.__collectionName]
