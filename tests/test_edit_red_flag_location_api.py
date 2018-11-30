import unittest
import json
from ..app import APP

BASE_URL = 'http://127.0.0.1:5000/api/v1/red-flags'
BAD_ITEM_URL = 'http://127.0.0.1:5000/api/v1/red-flags/10/location'
GOOD_ITEM_URL = 'http://127.0.0.1:5000/api/v1/red-flags/0/location'

class IReporterTestCase(unittest.TestCase):
    """This class represents the create red flag record test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP.test_client()
        self.app.testing = True


    def test_edit_location(self):
        location = {"location": "30.7788,78.999"}
        response = self.app.patch(GOOD_ITEM_URL,
                                data=json.dumps(location),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_edit_location_error(self):
        # location field cannot take int
        location = {"location": 30.000}
        response = self.app.patch(GOOD_ITEM_URL,
                                data=json.dumps(location),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # cannot edit non-existing item
        location = {"location": "0.133335,32.08777"}
        response = self.app.patch(BAD_ITEM_URL,
                                data=json.dumps(location),
                                content_type='application/json')
        self.assertEqual(response.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()