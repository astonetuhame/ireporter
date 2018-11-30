import unittest
import json
from app import APP

BASE_URL = 'http://127.0.0.1:5000/api/v1/red-flags'

class IReporterTestCase(unittest.TestCase):
    """This class represents the create red flag record test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP.test_client()
        self.app.testing = True


    def test_get_red_flags(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['data']), 2)
       

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()