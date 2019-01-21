'''This module represents the question view'''
from flask import abort,make_response,json
from json import dumps
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import reqparse, Resource

from app.api.v2.models.meetup_model import MeetupModel
from app.api.v2.models.user_model import UserModel
from app.api.v2.models.question_model import QuestionModel
from app.api.v2.utils.validator import ValidationHandler

class Question(Resource):
    '''Question requests'''
    @jwt_required
    def post(self, meetup_id):
        '''Create a question record'''
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True, help="title cannot be blank!")
        parser.add_argument('body', required=True, help="body cannot be blank!")
        parser.add_argument('created_by', required=True, help="body cannot be blank!")
        data = parser.parse_args()

        current_user = get_jwt_identity()
        user = UserModel().get_user_by_username(current_user)
        if not user:
            abort(401, 'This action requires loggin in!')


        question = {
            "created_by":UserModel().get_user_by_username(current_user),
            "meetup":meetup_id,
            "title":data['title'],
            "body":data['body']
        }
           
         # Validate the title
        ValidationHandler.validate_meetup_title(data['title'])

         # Validate the body
        ValidationHandler.validate_meetup_body(data['body'])

        if meetup_id.isdigit():
            meetup = MeetupModel().get_meetup_by_id(int(meetup_id))
            if meetup == {}:
                abort(404, "Meetup with id '{}' doesn't exist!".format(meetup_id))
            QuestionModel().add_question(question, meetup_id)
            meetup['questions'] += 1
            response = make_response(json.dumps(meetup), 200)
            response.headers.set('Content-Type', 'application/json')
            return response
        abort(400, 'meetup ID must be an integer value')
        return None

class Upvote(Resource):
    '''Upvotes requests'''
    @jwt_required
    def patch(self, meetup_id, question_id):
        '''Increase the vote of a question by 1'''
        meetup = MeetupModel().get_meetup_by_id(int(meetup_id))
        if meetup == {}:
            abort(404, "Meetup with ID '{}' doesn't exist!".format(meetup_id))
        question = MeetupModel().get_question_by_id(meetup, int(question_id))
        if question == {}:
            abort(404, "Question with ID '{}' doesn't exist!".format(question_id))
        question["upvotes"] += 1
        return {
            "status": 200,
            "data": [
                {
                    "meetup": meetup_id,
                    "title": question["title"],
                    "body": question["body"],
                    "upvotes": question["upvotes"]
                }
            ]
        }, 200

class Downvote(Resource):
    '''Downvotes requests'''
    @jwt_required
    def patch(self, meetup_id, question_id):
        '''Decrease the vote of a question by 1'''
        meetup = MeetupModel().get_meetup_by_id(int(meetup_id))
        if meetup == {}:
            abort(404, "Meetup with ID '{}' doesn't exist!".format(meetup_id))
        question = MeetupModel().get_question_by_id(meetup, int(question_id))
        if question == {}:
            abort(404, "Question with ID '{}' doesn't exist!".format(question_id))
        question["downvotes"] += 1
        return {
            "status": 200,
            "data": [
                {
                    "meetup": meetup_id,
                    "title": question["title"],
                    "body": question["body"],
                    "downvotes": question["downvotes"]
                }
            ]
        }, 200