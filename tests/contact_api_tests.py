
import sys
import unittest
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from mock import patch
sys.path.insert(0, sys.path[0] + "/..")

import app.app as plivo_apis
from config import app_config as cfg
from test_helpers import contact_api_helper

client = MongoClient('localhost', 27017)

def reinitializeTestSetup(client):
    client.drop_database("contactbook_test")
    db = client['contactbook_test']
    

class TestContactAPI(unittest.TestCase):
    def setUp(self):
        reinitializeTestSetup(client)
        self.test_client = plivo_apis.app.test_client()

    def test_all_contact_apis(self):
        email = "SHailed@gdmails.com"
        name = "Shailenda Singh"
        phone = "93414144"

        #Testing Post Request OF Contact API
        contanctCreated = contact_api_helper.Contact(self.test_client, email, name, phone)

        #Testing PUT Request OF Contact API
        phone = "111111111"
        contanctCreated = contanctCreated.update(self.test_client, email, name, phone)

        #Testing DELETE Request OF Contact API
        contanctCreated = contanctCreated.delete(self.test_client)
