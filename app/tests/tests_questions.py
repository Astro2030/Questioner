import unittest
import json
from app import create_app
import os


class QuestionsTestCase(unittest.TestCase):
    def setUp(self):
        '''Define test variables and initialize app'''
        self.app = create_app(config_name="testing")
        self.client = create_app('testing').test_client()

        self.data = {"createdOn": "19/10/09",
                     "createdBy": "Maggie",
                     "meetup": 20,
                     "topic": "Tech",
                     "status": "Answered"
                     }

    def test_create_question(self):
        '''Test if user can create a question'''
        response = self.client.post(
            'api/v1/questions', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)