'''Module for handling validations'''
from email_validator import validate_email, EmailNotValidError
from flask import abort
import re

has_space = re.compile(r'\s')

class ValidationHandler:
    '''Methods to validate the data provided by the API'''
    @staticmethod
    def validate_correct_username(username):
        '''Validation for a name'''
        print('validating usernme', username)
        if username.isdigit():
            abort(400, 'username cannot consist of digits only')
        if not username or not username.split():
            abort(400, 'username cannot be empty')
        if len(username) < 5 :
            abort(400, "Username should have more than five characters")
        if re.search(has_space, username):
            abort(400,"username should not have spaces")

    @staticmethod
    def validate_existing_user(users, username):
        '''Validation for an existing user'''
        if next(filter(lambda u: u['username'] == username, users), None):
            abort(409, "A user with username '{}' already exists!".format(username))

    @staticmethod
    def validate_existing_email(users, email):
        '''Validation for an existing email'''
        if next(filter(lambda u: u['email'] == email, users), None):
            abort(409, "The email address is already taken")

    @staticmethod
    def validate_firstname(firstname):
        '''Validation for an existing user'''
        if firstname.isdigit():
            abort(400, 'firstname cannot consist of digits only')
        if not firstname or not firstname.split():
            abort(400, 'firstname cannot be empty')
        if firstname.isspace():
            abort(400, 'firstname should not contain spaces.')
        if re.search(has_space, firstname):
            abort(400,"firstname should not have spaces")



    @staticmethod
    def validate_lastname(lastname):
        '''Validation for an existing user'''
        if lastname.isdigit():
            abort(400, 'lastname cannot consist of digits only')
        if not lastname or not lastname.split():
            abort(400, 'lastname cannot be empty')
        if lastname.isspace():
            abort(400, 'Lastname should not contain spaces.')
        if re.search(has_space, lastname):
            abort(400,"lastname should not have spaces")
        

    @staticmethod
    def validate_password(password):
        '''Validation for a password'''
        if not password or not password.split():
            abort(400, "password cannot be empty")
        if len(password) < 5 :
            abort(400, "password should have more than five characters")

    @staticmethod
    def validate_email_address(email):
        '''Validation for an email address'''
        try:
            v_email = validate_email(email)
            email = v_email["email"]
        except EmailNotValidError as email_valid_error:
            abort(400, str(email_valid_error))


    @staticmethod
    def validate_meetup_topic(topic):
        '''Validation for an existing user'''
        if topic.isdigit():
            abort(400, 'topic cannot consist of digits only')
        if not topic or not topic.split():
            abort(400, 'topic cannot be empty')

    @staticmethod
    def validate_meetup_location(location):
        '''Validation for an existing user'''
        if location.isdigit():
            abort(400, 'topic cannot consist of digits only')
        if not location or not location.split():
            abort(400, 'location cannot be empty')

    @staticmethod
    def validate_meetup_title(title):
        '''Validation for an existing user'''
        if title.isdigit():
            abort(400, 'title cannot consist of digits only')
        if not title or not title.split():
            abort(400, 'title cannot be empty')

    @staticmethod
    def validate_meetup_body(body):
        '''Validation for an existing user'''
        if body.isdigit():
            abort(400, 'body cannot consist of digits only')
        if not body or not body.split():
            abort(400, 'body cannot be empty')

    