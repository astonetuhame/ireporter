import unittest
import json
from ..app import APP

BASE_URL = 'http://127.0.0.1:5000/api/v1/red-flags'

class IReporterTestCase(unittest.TestCase):
    """This class represents the create red flag record test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP.test_client()
        self.app.testing = True


    def test_create_red_flag_record(self):
        # missing other input fields
        user = {          
            "createdBy" : 1,
            "type" : "red-flag",
            "Images" : ["myimage.jpg"],
            "Videos": ["myvideo.mp4"],
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(user),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        # input fields; location, type cannot take int only str
        incident = {
            "createdBy" : 1,
            "type" : 888,
            "location" : 2224,
            "Images" : ["myimage.jpg"],
            "Videos": ["myvideo.mp4"],
            "comment": 8458
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Please use character strings')
        self.assertEqual(response.status_code, 400)
        # type field should be red-flag or intervention
        incident = {
            "createdBy" : 1,
            "type" : "corruption",
            "location" : "300.178,12.00",
            "Images" : ["myimage.jpg"],
            "Videos": ["myvideo.mp4"],
            "comment": "Government stole money"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Input red-flag or intervention')
        self.assertEqual(response.status_code, 400)
        # location, comment field should contain atleast a character
        incident = {
            "createdBy" : 1,
            "type" : "red-flag",
            "location" : "",
            "Images" : ["myimage.jpg"],
            "Videos": ["myvideo.mp4"],
            "comment": ""
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Field should atleast contain a character')
        self.assertEqual(response.status_code, 400)
        # location ot type field should not contain spaces
        incident = {
            "createdBy" : 1,
            "type" : "red-flag ",
            "location" : "45.8888",
            "Images" : ["myimage.jpg"],
            "Videos": ["myvideo.mp4"],
            "comment": "government should be serious"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'No whitespaces allowed')
        self.assertEqual(response.status_code, 400)
        # createdBy field should be int type only
        incident = {
            "createdBy" : "jjjj",
            "type" : "red-flag",
            "location" : "45.8888",
            "Images" : ["myimage.jpg"],
            "Videos": ["myvideo.mp4"],
            "comment": "government should be serious"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Please use integer values')
        self.assertEqual(response.status_code, 400)
        # images or videos should be of type list
        incident = {
            "createdBy" : 1,
            "type" : "red-flag",
            "location" : "45.8888",
            "Images" : 123,
            "Videos": "ssss",
            "comment": "government should be serious"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Image or Video should be a list')
        self.assertEqual(response.status_code, 400)
        # images list values should be of string type
        incident = {
            "createdBy" : 1,
            "type" : "red-flag",
            "location" : "45.8888",
            "Images" : [7,8,9],
            "Videos": ["a.mp4", "b.mp4"],
            "comment": "government should be serious"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Character strings needed for Images sequence')
        self.assertEqual(response.status_code, 400)
        # videos list values should be of string type
        incident = {
            "createdBy" : 1,
            "type" : "red-flag",
            "location" : "45.8888",
            "Images" : ["a.jpg", "b.mp4"],
            "Videos": [1,2,3],
            "comment": "government should be serious"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Character strings needed for Videos sequence')
        self.assertEqual(response.status_code, 400)
        # images list should not be empty
        incident = {
            "createdBy" : "ash",
            "type" : "red-flag",
            "location" : "45.8888",
            "Images" : [""],
            "Videos": ["1.mp4","2.mp4","b.mp4"],
            "comment": "government should be serious"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Image cannot be empty')
        self.assertEqual(response.status_code, 400)
        # videos list should not be empty
        incident = {
            "createdBy" : "ash",
            "type" : "red-flag",
            "location" : "45.8888",
            "Images" : ["mine.jpg"],
            "Videos": [""],
            "comment": "government should be serious"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(data['error'], 'Video cannot be empty')
        self.assertEqual(response.status_code, 400)
        # valid data should be accepted
        incident = {
               "createdBy" : 1,
                "type" : "red-flag",
                "location" : "30.178,12.00",
                "Images" : ["myimage.jpg"],
                "Videos": ["myvideo.mp4"],
                "comment": "Government stole money"
            }
        response = self.app.post(BASE_URL,
                                 data=json.dumps(incident),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()