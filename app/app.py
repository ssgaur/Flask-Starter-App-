#!/usr/bin/python

import sys
sys.path.insert(0, sys.path[0] + "/..")
from config import app_config as cfg

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask.views import MethodView
from functools import wraps

from services import contactService
from services import userService

app = Flask(__name__)
CORS(app)

URL = "/api/v1/"


def auth(function):
    @wraps(function)
    def wrap_function(*args, **kwargs):
        headerInfo = request.headers
        status = {}
        status['type'] = 'Fail'
        status['message'] = 'Unauthorised'

        if "email" not in headerInfo:
            return jsonify({'status': status}), 401

        userObj = userService.User()
        if not userObj.isCorrectUser(headerInfo['email']):
            return jsonify({'status': status}), 401

        return function(*args, **kwargs)
    return wrap_function

@app.route('/api/v1/user/register', methods=['POST'])
def user_register():
    userObj = userService.User()
    return userObj.create()

@app.route('/api/v1/user/login', methods=['POST'])
def user_login():
    userObj = userService.User()
    return userObj.login()


@app.route('/api/v1/contact', methods=['POST'])
def contact_create():
    contactObj = contactService.Contact()
    return contactObj.create()


@app.route('/api/v1/contact/<contact_id>', methods=['PUT'])
def contact_update(contact_id):
    contactObj = contactService.Contact()
    return contactObj.update(contact_id)

@app.route('/api/v1/contact/<contact_id>', methods=['DELETE'])
def contact_delete(contact_id):
    contactObj = contactService.Contact()
    return contactObj.delete(contact_id)

@app.route('/api/v1/contact/search', methods=['GET'])
@auth
def contact_search():
    contactObj = contactService.Contact()
    return contactObj.search()

if __name__ == '__main__':
    app.run(host=cfg.host, port=cfg.port, threaded=True, debug=True)
