from DBClient import DBClient
from bson import ObjectId
from pymongo import IndexModel, ASCENDING, DESCENDING, errors

class Database(object):
    def __init__(self, collectionName):
        try:
            self.__collection = DBClient(collectionName).getCollectionInstance()
        except errors.PyMongoError as e:
            raise errors.ConnectionFailure('Error in connection to Database %s' % (e.message))

    
    def insertOneDocument(self, data):
        try:
            created_id =  self.__collection.insert_one(data).inserted_id
            return str(created_id)
        except errors.PyMongoError as e:
            raise errors.WriteError('Error in Creating Document %s' % (e.message))

    def getById(self, _id, fields={}):
        if fields == {}:
            fields = None
        result =  self.__collection.find_one({'_id' : ObjectId(_id)})
        if result is not None:
            result['_id'] = str(result['_id'])
        return result

    def getByEmail(self, email):
        result =  self.__collection.find_one({'email' : email})
        if result is not None:
            result['_id'] = str(result['_id'])
        return result

    def customGet(self, fields):
        result =  self.__collection.find_one(fields)
        if result is not None:
            result['_id'] = str(result['_id'])
        return result

    def updateById(self, id, data):
        try:
            self.__collection.update({'_id': ObjectId(id)}, {'$set': data})
            return True
        except errors.PyMongoError as e:
            raise errors.WriteError('Error in updating Document %s' % (e.message))

    def deleteById(self, _id):
        try:
            self.__collection.delete_one({'_id': ObjectId(_id)})
            return True
        except errors.PyMongoError as e:
            raise errors.WriteError('Error in deleting Document %s' % (e.message))


    def getDocumentsCount(self, query={}):
        if query != {}:
            return self.__collection.find(query).count()
        else:
            return self.__collection.count()

    def paginationQuery(self, filters={}, fields={}, skip=0, limit=100, sortParams=['_id', 1]):
        if fields == {}:
            fields = None
        return list(
            self.__collection.find(filters, fields).skip(skip).limit(limit).sort(sortParams[0],sortParams[1])
        )
    