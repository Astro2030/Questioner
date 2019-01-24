'''This module represents the user view'''
from flask import abort
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash,check_password_hash
from app.api.v2.utils.validator import ValidationHandler
from app.api.v2.models.user_model import UserModel

class UserRegistration(Resource):
    """Register a new user"""
    def post(self):
        """Create a user account"""
        parser = reqparse.RequestParser()
        parser.add_argument('firstname', type=str, required=True, help='firstname cannot be blank!')
        parser.add_argument('lastname', type=str, required=True, help='lastname cannot be blank!')
        parser.add_argument('email', type=str, required=True, help='email cannot be blank!')
        parser.add_argument('username', type=str, required=True, help='username cannot be blank!')
        parser.add_argument('password', type=str, required=True, help='password cannot be blank!')
        parser.add_argument('confirm_password', type=str, required=True, help='password cannot be blank!')


        data = parser.parse_args()

        user=UserModel()
        firstname=data['firstname']
        lastname=data['lastname']
        username = data['username']
        password = data['password']
        confirm_password = data['confirm_password']
        email = data['email']

        # Validate the firstname
        ValidationHandler.validate_firstname(firstname)

         # Validate the lastname
        ValidationHandler.validate_firstname(lastname)

         # Validate the username
        ValidationHandler.validate_correct_username(username)

        # Validate the email address
        ValidationHandler.validate_email_address(email)

        # Validate the password
        ValidationHandler.validate_password(password)

        # confirm password match
        ValidationHandler.verify_password_match(password, confirm_password)
        users = UserModel().get_all_users()

        user_details = {
            'firstname':data['firstname'],
            'lastname':data['lastname'],
            'username': data['username'],
            'password' : generate_password_hash(data['password']),
            'email' : data['email']
        }
        ValidationHandler.validate_existing_user(users, username)
        new_user = user.add_user(user_details)

        val = UserModel().get_user_by_username(username)
        print(val)
        print(new_user)
        return {
                "status": 201,
                "data": [
                    {   
                        "message" : "User is successfully created"
                    }
                ]
            }, 201

class UserLogin(Resource):
    '''Log in a user'''
    def post(self):
        '''Sign In a registered user'''
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help='username cannot be empty!')
        parser.add_argument('password', type=str, required=True, help='password cannot be empty!')

        data = parser.parse_args()

        current_user = UserModel().get_user_by_username(data['username'])
        ValidationHandler.validate_correct_username(data['username'])
        if not current_user:
            abort(404, "User with username '{}' doesn't exist!".format(data['username']))
        if check_password_hash(current_user['password'], data['password']):
            access_token = create_access_token(identity=data['username'])
            return {
                    'status':200,
                    "data":[

                        {
                            'message' : "Logged in as '{}'".format(current_user['username']),
                            'access_token' : access_token
                        }
                    ]
            }, 200
        abort(401, 'Wrong credentials')
        return None
