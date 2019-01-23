import json
import unittest
import pytest

from datetime import datetime
from app.api.v2.models.db import init_db_command
from app import create_app
from app.api.v2.models.user_model import UserModel

class BaseTestCase(unittest.TestCase):
    '''Base class for other test classes'''
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

        self.user_registration = dict(
            firstname="test_first",
            lastname="test_last",
            email="test@example.com",
            username="username",
            password="Venter@omari",
            confirm_password="Venter@omari"
        )

        self.digit_username = dict(
            firstname="test_first",
            lastname="test_last",
            email="test@example.com",
            username="1234",
            password="Venter@omari",
            confirm_password="Venter@omari"    

        )

        self.empty_username = dict(
            firstname="test_first",
            lastname="test_last",
            email="test@example.com",
            username="",
            password="Venter@omari",
            confirm_password="Venter@omari"
        )

        self.empty_password = dict(
            firstname="test_first",
            lastname="test_last",
            email="test@example.com",
            username="username",
            password="",
            confirm_password=""
        )

        self.wrong_email_registration = dict(
            firstname="test_first",
            lastname="test_last",
            email="testexample.com",
            username="username",
            password="Venter@omari",
            confirm_password="Venter@omari"
        )

        self.user_login = dict(username="username", password="Venter@omari")
        self.wrong_password = dict(username="username", password="abcde")

        self.meetup = dict(
            location="Test Location",
            topic="Test Topic",
            happening_on="Jan 10 2019 3:30PM",
            description = "description cannot be blank!"
        )

        self.new_meetup = dict(
            location="Test New Location",
            topic="Test New Topic",
            happening_on="Jan 15 2019 11:00AM",
            description = "description cannot be blank!"
        )

        self.question = dict(
            title="test title",
            body="test body"
        )

        self.rsvp = dict(response="maybe")

    def get_accept_content_type_headers(self):
        '''Return the content type headers for the body'''
        content_type = {}
        content_type['Accept'] = 'application/json'
        content_type['Content-Type'] = 'application/json'
        return content_type

    def get_authentication_headers(self, access_token):
        '''Return the authentication header'''
        authentication_headers = self.get_accept_content_type_headers()
        authentication_headers['Authorization'] = "Bearer {}".format(access_token)
        return authentication_headers

    def get_access_token(self, user_registration, user_login):
        '''Fetch access token from user login'''
        self.client().post(
            'api/v2/auth/register',
            headers=self.get_accept_content_type_headers(),
            data=json.dumps(self.user_registration)
        ) # User Registration
        res = self.client().post(
            'api/v2/auth/login',
            headers=self.get_accept_content_type_headers(),
            data=json.dumps(self.user_login)
        ) # User Log In
        response_msg = json.loads(res.data.decode("UTF-8"))
        access_token = response_msg["access_token"]
        return access_token

    def create_meetup(self, access_token, meetup):
        '''Create a meetup record'''
        self.client().post(
            '/api/v2/meetups',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(meetup)
        )

    def create_question(self, access_token, question):
        '''Create a question record'''
        self.client().post(
            '/api/v2/meetups/1/questions',
            headers=self.get_authentication_headers(access_token),
            data=json.dumps(question)
        )
    def tear_down(self):
        destroy_database()

if __name__ == "__main__":
    unittest.main()