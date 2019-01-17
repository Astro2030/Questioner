'''This module represents a user entity'''
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2.extras import RealDictCursor
from app.api.v2.utils.utility import Utility
from .db import get_database

# USERS = [] # Data store for the users

class UserModel():
    '''Entity representation for a user'''
    def __init__(self):
        '''initialize db connection'''
        self.conn = get_database()

    def get_user_id(self, id):
        '''Fetch a user by id'''
        query_string = 'SELECT * FROM users WHERE id = %d;'
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (id,))
        return cursor.fetchone()

    @staticmethod
    def generate_password_hash(password):
        '''Generate the hash of the password'''
        return sha256.hash(password)

    @staticmethod
    def verify_password_hash(password, hashed_password):
        '''Compare the password with its hashed value'''
        return sha256.verify(password, hashed_password)

    # @staticmethod
    def add_user(self,user):
        '''Add a new user to the data store'''
        
        return self.conn.cursor().execute("""
            INSERT INTO users (firstname, lastname, username, email,password, is_admin) VALUES (%(firstname)s, %(lastname)s, %(username)s, %(email)s, \
            %(password)s, %(is_admin)s);""",user)

    # @staticmethod
    def get_all_users(self):
        '''Fetch all users'''
        query_string = 'SELECT * FROM users;'
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string)
        return cursor.fetchall()

    @staticmethod
    def get_user_by_username(username):
        '''Fetch a user given a username'''
        return Utility.fetch_item(username, 'username', USERS)