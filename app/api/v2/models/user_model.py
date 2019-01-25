'''This module represents a user entity'''
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256
from psycopg2.extras import RealDictCursor
from .db import get_database

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

    def add_user(self,user):
        '''Add a new user to the data store'''
        return self.conn.cursor().execute("""
            INSERT INTO users (firstname, lastname, username, email, password) VALUES (%(firstname)s, %(lastname)s, %(username)s, %(email)s, \
            %(password)s);""",user)

    def get_all_users(self):
        '''Fetch all users'''
        query_string = 'SELECT * FROM users;'
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string)
        return cursor.fetchall()

    def get_user_by_username(self, username):
        '''Fetch a user given a username'''
        query_string = "SELECT * FROM users WHERE username = %s;"
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (username,))
        return cursor.fetchone()

    def get_email(self, email):
        '''check if email exists'''
        query_string = "SELECT * FROM users WHERE email = %s;"
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (email,))
        return cursor.fetchone()