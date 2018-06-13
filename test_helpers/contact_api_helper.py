from __future__ import print_function
import json

def getContactInfor(email, name, phone):
    contactInfo = {
        "email" : email,
        "name" : name,
        "phone": phone
    }
    return contactInfo


class Contact(object):
    _id = None
    contactInfo = None

    def __init__(self, test_client, name, email, phone):
        contactInfo = getContactInfor(name, email, phone)
        print("Contact being sent in request is %s" % (contactInfo))
        response = test_client.post('http://localhost:7000/api/v1/contact', data=json.dumps(contactInfo))
        assert response.status_code == 200, "Contact creation failed"
        print("Contact Creation returned = %s" % (json.loads(response.data)))
        self._id = json.loads(response.data)['data'][0]
        print("ID returned from Contact Creation is %s" % (self._id))
        self.contactInfo = contactInfo

    def update(self, test_client, name, email, phone):
        contactInfo = getContactInfor(name, email, phone)
        print("Contact being sent in edit is %s" % (contactInfo))
        r = test_client.put('http://localhost:7000/api/v1/contact/' + self._id, data=json.dumps(contactInfo))
        print ("Comtact Edit returned = %s" % (r))
        assert r.status_code == 200, "Contact Update failed"
        self.contactInfo = contactInfo
    
    def delete(self, test_client, expectedStatusCode = 200):
        r = test_client.delete('http://localhost:7000/api/v1/contact/ ' + self._id)
        assert r.status_code == expectedStatusCode

    def getId(self):
        return self._id


