'''This module represents the question entity'''
from datetime import datetime
from .db import get_database
from psycopg2.extras import RealDictCursor

from app.api.v2.models.meetup_model import MeetupModel

class QuestionModel:
    '''Entity representation for a question'''
    def __init__(self):
        '''initialize db connection'''
        self.conn = get_database()

    def add_question(self, questions):
        '''Add a new question to the data store'''
        return self.conn.cursor().execute("""
            INSERT INTO questions (title, body, meetup_id, created_by) VALUES (%(title)s, %(body)s, %(meetup_id)s, %(created_by)s);""",questions)

    def get_all_questions_by_meetup_id(self,meetup_id):
        '''Fetch all meetup questions'''
        query_string = 'SELECT * FROM questions WHERE meetup_id = %s;'
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (meetup_id,))
        return cursor.fetchall()

    def get_questions_by_meetup_id(self,meetup_id):
        '''Fetch all meetup questions'''
        query_string = 'SELECT * FROM questions WHERE meetup_id = %s;'
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (meetup_id,))
        return cursor.fetchone()

    def update_upvotes(self, question_id, Upvote):
        '''Increment votes'''
        query_string = 'update questions set upvotes = %(Upvote)s where id=%(question_id)s;'
        cursor = self.conn.cursor()
        return cursor.execute(query_string,{'question_id':question_id, 'Upvote':Upvote})

    def update_downvotes(self, question_id, Downvote):
        '''Increment votes'''
        query_string = 'update questions set upvotes = %(Upvote)s where id=%(question_id)s;'
        cursor = self.conn.cursor()
        return cursor.execute(query_string,{'question_id':question_id, 'Upvote':Downvote})

    def is_question_existing(self,title,body):
        """ doc """
        query_string ="SELECT * FROM questions where title=%s and body=%s;"
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query_string, (title,body))
        result = cursor.fetchall()
        return len(result)!=0


    

        