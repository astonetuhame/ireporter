import unittest
import os
import json
from ..app import APP

#BASE_URL = 'http://127.0.0.1:5000/api/v1.0/items'
BASE_URL = 'http://127.0.0.1:5000/api/v1/users'

class IReporterTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP.test_client()
        self.app.testing = True


    def test_create_account(self):
        # missing other input fields
        user = {"firstName": "some_item"}
        response = self.app.post(BASE_URL,
                                 data=json.dumps(user),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # input field cannot take int only str
        user = {
            "firstName" : 888,
            "lastName" : 99 ,
            "otherNames" : "Junior" ,
            "email" : "atuhame@gmail.com" ,
            "phoneNumber" : "0779219779",
            "username" : 66,
            "password": "12345"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(user),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Please use character strings')
        self.assertEqual(response.status_code, 400)
        # email must be valid
        user = {
            "firstName" : "aston",
            "lastName" : "tuhame" ,
            "otherNames" : "Junior" ,
            "email" : "atuhame@gmail" ,
            "phoneNumber" : "0779219779",
            "username" : "66",
            "password": "12345"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(user),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Invalid Email')                         
        self.assertEqual(response.status_code, 400)
        # valid: both required fields, value takes str
        user = {
                "firstName" : "Astone",
                "lastName" : "Tuhame" ,
                "otherNames" : "Junior" ,
                "email" : "atuhame@gmail.com" ,
                "phoneNumber" : "0779219779",
                "username" : "Taent",
                "password": "12345",
                }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(user),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        # check if data matches
        data = json.loads(response.get_data())
        self.assertEqual(data['user']['id'], 1)
        self.assertEqual(data['user']['email'], 'atuhame@gmail.com')
        # cannot add item with same email again
        user = {"firstName" : "Astone",
                "lastName" : "Tuhame" ,
                "otherNames" : "Junior" ,
                "email" : "atuhame@gmail.com" ,
                "phoneNumber" : "0779219779",
                "username" : "Taent",
                "password": "12345"
                }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(user),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # # input fields must not be empty
        # user = {
        #     "firstName" : "John",
        #     "lastName" : "Doe" ,
        #     "otherNames" : "" ,
        #     "email" : "" ,
        #     "phoneNumber" : "",
        #     "username" : "JohnDoe",
        #     "password": "1234",
        #     }
        # response = self.app.post(BASE_URL,
        #                          data=json.dumps(user),
        #                          content_type='application/json')
        # data = json.loads(response.get_data())
        # self.assertEqual(data['error'], 'Please fill in the fields')
        # self.assertEqual(response.status_code, 400)
        

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()