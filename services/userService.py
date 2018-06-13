from database import Database
from flask import request, jsonify


class User(object):
    def __init__(self):
        self.__userCollection = Database("users")
    
    def get(self):
        pass
    
    def create(self):
        userData = request.get_json(force=True)
        status = {}
        if 'email' not in userData or "password" not in userData:
            status['type'] = 'Fail'
            status['message'] = 'Email and Password Are required Fields'
            return jsonify({'data':[], 'status': status}), 400

        existingUser = self.__userCollection.getByEmail(userData['email'])
        if existingUser is not None:
            status['type'] = 'Fail'
            status['message'] = 'Email Already Exists'
            return jsonify({'data':[], 'status': status}), 400
        
        user_id = self.__userCollection.insertOneDocument(userData)

        status['type'] = 'success'
        status['message'] = 'User is registered successfully'
        return jsonify({'data':user_id, 'status': status}), 200

    def login(self):
        userData = request.get_json(force=True)
        status = {}

        if 'email' not in userData or "password" not in userData:
            status['type'] = 'Fail'
            status['message'] = 'Email and Password Are required Fields'
            return jsonify({'data':[], 'status': status}), 400
        query = {
            "email": userData["email"],
            "password": userData["password"]
        }
        userData = self.__userCollection.customGet(query)
        if userData is not None:
            status['type'] = 'success'
            status['message'] = 'User Logged in successfully'
            return jsonify({'data':[], 'status': status}), 200
        else:
            status['type'] = 'Faile'
            status['message'] = 'Invalid Credntialas'
            return jsonify({'data':[], 'status': status}), 200

    def isCorrectUser(self, email):
        existingUser = self.__userCollection.getByEmail(email)
        if existingUser is not None:
            return True
        else:
            return False

    def delete(self):
        pass