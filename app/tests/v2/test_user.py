'''This module represents tests for the user entity'''
import json
from app.api.v2.models.user_model import UserModel
from app.tests.v2.test_base import BaseTestCase

class UserTestCase(BaseTestCase):
    '''Test definitions for a user'''
    def test_digit_username(self):
        '''
        Test the API cannot register a user with a username consisting of digits only
        '''
        res = self.client().post(
            'api/v2/auth/register',
            headers=self.get_accept_content_type_headers(),
            data=json.dumps(self.digit_username)
        )
        self.assertEqual(res.status_code, 400)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(response_msg["message"], "username cannot consist of digits only")

    def test_empty_username(self):
        '''
        Test the API cannot register a user with an empty username
        '''
        res = self.client().post(
            'api/v2/auth/register',
            headers=self.get_accept_content_type_headers(),
            data=json.dumps(self.empty_username)
        )
        self.assertEqual(res.status_code, 400)
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(response_msg["message"], "username cannot be empty")

    def test_invalid_email_address_registration(self):
        '''
        Test the API cannot register a user with an invalid email address
        '''
        res = self.client().post(
            'api/v2/auth/register',
            headers=self.get_accept_content_type_headers(),
            data=json.dumps(self.wrong_email_registration)
        )
        response_msg = json.loads(res.data.decode("UTF-8"))
        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            response_msg['message'],
            "The email address is not valid. It must have exactly one @-sign."
        )

    def test_username_login(self):
        '''Test the API can log in a user'''
        res = self.client().post(
            'api/v2/auth/register',
            headers=self.get_accept_content_type_headers(),
            data=json.dumps(self.user_registration)
        )
        self.assertEqual(res.status_code, 201)
        res = self.client().post(
            'api/v2/auth/login',
            headers=self.get_accept_content_type_headers(),
            data=json.dumps(self.user_login)
        )
        self.assertEqual(res.status_code, 200)

    