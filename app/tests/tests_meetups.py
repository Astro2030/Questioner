import unittest
import json
from app import create_app
import os


class MeetupsTestCase(unittest.TestCase):
    def setUp(self):
        '''Define test variables and initialize app'''
        self.app = create_app(config_name="testing")
        self.client = create_app('testing').test_client()
        self.data = {
            "meetup_id": 1,
            "createdOn": "10/10/10",
            "location": "kenya",
            "topic": "immigration",
            "happeningOn": "10/10/10",
            "tags": "API"
        }

    def test_get_all_meetups(self):
        '''Test if user can get all meetup records'''
        response = self.client.get(
            'APP/v1/meetups', content_type="application/json")
        self.assertEqual(response.status_code, 200)

'''Standard unittest runner for executing the test'''
if __name__ == '__main__':
    unittest.main()