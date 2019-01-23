'''This module represents the meetup view'''
from flask import abort,json,make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import reqparse, Resource
from json import dumps
from flask import jsonify

from app.api.v2.models.meetup_model import MeetupModel
from app.api.v2.models.user_model import UserModel
from app.api.v2.utils.validator import ValidationHandler
from app.api.v2.utils.route_protector import admin_required

class MeetupList(Resource):
    '''Request on a meetup list'''
    @jwt_required
    @admin_required
    def post(self):
        '''Create a meetup record'''
        parser = reqparse.RequestParser()
        parser.add_argument('location', required=True, help="location cannot be blank!")
        parser.add_argument('topic', required=True, help="location cannot be blank!")
        parser.add_argument('happening_on', required=True, help="location cannot be blank!")
        parser.add_argument('description', required=True, help="description cannot be blank!")
        data = parser.parse_args()

        current_user = get_jwt_identity()
        user = UserModel().get_user_by_username(current_user)
        if not user:
            abort(401, 'This action requires loggin in!')

        meetup = {
            "location":data['location'],
            "description":data['description'],
            "topic":data['topic'],
            "happening_on":MeetupModel.convert_string_to_date(data['happening_on']),
        }

        # Validate the location
        ValidationHandler.validate_meetup_location(data['location'])

        # Validate the topic
        ValidationHandler.validate_meetup_topic(data['topic'])
        is_meet_up_extisting = MeetupModel().is_meet_up_existing(
            meetup["location"],
            meetup["topic"],
            meetup["happening_on"]
            )
        if is_meet_up_extisting:
            abort(409, 'This meetup has already been scheduled') 
        
        MeetupModel().add_meetup(meetup)
        return {
            'status': 201,
            'data': meetup
        }, 201


class Meetup(Resource):
    '''Request on a meetup item'''
    @jwt_required
    def get(self, meetup_id):
        '''Fetch a single meetup item'''
        if meetup_id.isdigit():
            meetup = MeetupModel().get_meetup_by_id(meetup_id)
            if meetup == {}:
                abort(404, "Meetup with id '{}' doesn't exist!".format(meetup_id))
            response = make_response(json.dumps(meetup), 200)
            response.headers.set('Content-Type', 'application/json')
            return response
        abort(400, 'Meetup ID must be an Integer')
        return None


class UpcomingMeetup(Resource):
    '''Request on an upcoming meetup item'''
    @jwt_required
    def get(self):
        '''Fetch all upcoming meetups'''
        meetup = MeetupModel().get_all_meetups()
        if not meetup:
            abort(404, 'No meetup is available')
        response = make_response(json.dumps(meetup), 200)
        response.headers.set('Content-Type', 'application/json')
        return response
