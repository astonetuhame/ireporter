import unittest
import json
from ..app import APP

BASE_URL = 'http://127.0.0.1:5000/api/v1/red-flags'
BAD_ITEM_URL = 'http://127.0.0.1:5000/api/v1/red-flags/10/comment'
GOOD_ITEM_URL = 'http://127.0.0.1:5000/api/v1/red-flags/0/comment'

class IReporterTestCase(unittest.TestCase):
    """This class represents the create red flag record test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP.test_client()
        self.app.testing = True


    def test_edit_comment(self):
        comment = {"comment": "30.7788,78.999"}
        response = self.app.patch(GOOD_ITEM_URL,
                                data=json.dumps(comment),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_edit_comment_error(self):
        # comment field cannot take int
        comment = {"comment": 30.000}
        response = self.app.patch(GOOD_ITEM_URL,
                                data=json.dumps(comment),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # cannot edit non-existing item
        comment = {"comment": "government is bad"}
        response = self.app.patch(BAD_ITEM_URL,
                                data=json.dumps(comment),
                                content_type='application/json')
        self.assertEqual(response.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()