from database import Database
from flask import request, jsonify
from services import pagination

class Contact(object):
    def __init__(self):
        self.__contactCollection = Database("contacts")
    
    def search(self):
        searchTerm = str(request.args.get('searchTerm', default=''))
        status = {}
        query = {
                    "$or": [
                            {"email": {'$regex': searchTerm, '$options': 'i'} } ,
                            {"name": {'$regex': searchTerm, '$options': 'i'} } 
                        ]
                }

        results, paginationInfo = pagination.Pagination().do(self.__contactCollection, query, request)
        status['type'] = 'success'
        status['message'] = 'Contact is Added successfully'
        return jsonify({'data':results, 'paginationInfo':paginationInfo, 'status': status}), 200
    
    def create(self):
        contactData = request.get_json(force=True)
        status = {}
        if 'email' not in contactData:
            status['type'] = 'Fail'
            status['message'] = 'Email Are required Fields'
            return jsonify({'data':[], 'status': status}), 400

        existingContact = self.__contactCollection.getByEmail(contactData['email'])
        if existingContact is not None:
            status['type'] = 'Fail'
            status['message'] = 'Contact With Given Email Already Exists'
            return jsonify({'data':[], 'status': status}), 400
        
        contact_id = self.__contactCollection.insertOneDocument(contactData)

        status['type'] = 'success'
        status['message'] = 'Contact is Added successfully'
        return jsonify({'data':[contact_id], 'status': status}), 200
    
    def update(self, contact_id):
        contactData = request.get_json(force=True)
        status = {}

        if contact_id is None: 
            status['type'] = 'Fail'
            status['message'] = 'Contact Id Are required Field'
            return jsonify({'data':[], 'status': status}), 400

        existingContact = self.__contactCollection.getById(contact_id)

        if existingContact is None:
            status['type'] = 'Fail'
            status['message'] = 'No Contact is Found with given Id'
            return jsonify({'data':[], 'status': status}), 400

        print contactData["email"]
        print existingContact["email"]
        if "email" in contactData:
            if contactData["email"] != existingContact["email"]:
                status['type'] = 'Fail'
                status['message'] = 'Email Can not be changed'
                return jsonify({'data':[], 'status': status}), 400
        
        self.__contactCollection.updateById(contact_id, contactData)
        
        status['type'] = 'success'
        status['message'] = 'Contact is Updated successfully'
        return jsonify({'data':contact_id, 'status': status}), 200

    def delete(self, contact_id):
        contactData = request.get_json(force=True)
        status = {}

        if contact_id is None: 
            status['type'] = 'Fail'
            status['message'] = 'Contact Id Are required Field'
            return jsonify({'data':[], 'status': status}), 400

        self.__contactCollection.deleteById(contact_id)

        status['type'] = 'success'
        status['message'] = 'Contact is Deleted successfully'
        return jsonify({'data':contact_id, 'status': status}), 200