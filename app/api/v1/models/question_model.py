'''This module represents the question entity'''
from datetime import datetime
from app.api.v1.utils.serializer import serialize
from app.api.v1.models.meetup_model import MeetupModel

ALL_QUESTIONS = [] # Data store for the questions

class QuestionModel:
    '''Entity representation for a question'''
    def __init__(self, Author, meetup, title, body):
        self.question_id = len(ALL_QUESTIONS) + 1
        self.created_on = str(datetime.utcnow())
        self.Author = Author
        self.meetup = meetup
        self.title = title
        self.body = body
        self.upvotes = 0
        self.downvotes = 0

    @staticmethod
    def add_question(question, meetup_id):
        '''Add a new question to the data store'''
        ALL_QUESTIONS.append(question)
        meetup = MeetupModel.get_meetup_by_id(int(meetup_id))
        meetup["questions"].append(serialize(question))
