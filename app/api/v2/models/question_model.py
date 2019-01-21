'''This module represents the question entity'''
from datetime import datetime
from .db import get_database
from psycopg2.extras import RealDictCursor

from app.api.v1.models.meetup_model import MeetupModel

class QuestionModel:
    '''Entity representation for a question'''
    def __init__(self):
        '''initialize db connection'''
        self.conn = get_database()

    def add_question(self, questions, meetup_id):
        '''Add a new question to the data store'''
        return self.conn.cursor().execute("""
            INSERT INTO questions (title, body, meetup_id) VALUES (%(title)s, %(body)s, %(meetup_id)d);""",questions)
        