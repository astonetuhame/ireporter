import unittest
import json
from app import APP

BASE_URL = 'http://127.0.0.1:5000/api/v1/red-flags'
BAD_ITEM_URL = 'http://127.0.0.1:5000/api/v1/red-flags/5'
GOOD_ITEM_URL = 'http://127.0.0.1:5000/api/v1/red-flags/1'

class IReporterTestCase(unittest.TestCase):
    """This class represents the create red flag record test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP.test_client()
        self.app.testing = True


    def test_delete(self):
        response = self.app.delete(GOOD_ITEM_URL)
        self.assertEqual(response.status_code, 200)
        response = self.app.delete(BAD_ITEM_URL)
        self.assertEqual(response.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()