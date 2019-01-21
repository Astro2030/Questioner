'''This module represents a meetup entity'''
from datetime import datetime
from .db import get_database
from psycopg2.extras import RealDictCursor

class MeetupModel:
    '''Entity representation for a meetup'''
    def __init__(self):
        '''initialize db connection'''
        self.conn = get_database()

    def get_meetup_id(self):
        '''Fetch a meetup by id'''
        query_string = 'SELECT * FROM meetup WHERE id = %d;'
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (id,))
        return cursor.fetchone()

    @staticmethod
    def convert_string_to_date(string_date):
        '''Convert string object to datetime object'''
        return str(datetime.strptime(string_date, '%b %d %Y %I:%M%p'))

    def add_meetup(self,meetup):
        '''Add a new meetup to the data store'''
        return self.conn.cursor().execute("""
            INSERT INTO meetup (location, topic, description, happening_on) VALUES (%(location)s, %(topic)s, %(description)s, %(happening_on)s);""",meetup)

    def get_meetup_by_id(self,id):
        '''Return a meetup given a meetup id'''
        query_string = "SELECT * FROM meetup WHERE id = %s;"
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (id,))
        return cursor.fetchone() 

    def get_all_meetups(self):
        '''Fetch all meetups'''
        query_string = 'SELECT * FROM meetup;'
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string)
        return cursor.fetchall()

    def get_question_by_id(self, meetup, id):
        '''Fetch a question by id'''
        query_string = "SELECT * FROM question WHERE id = %s;"
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (id,))
        return cursor.fetchone()