from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v1.models.meetupsmodel import all_meetups, Meetups, all_rsvps


class AllMeetupsApi(Resource):
    '''Endpoint for all meetups functionality'''

    def post(self):
        data = request.get_json(force=True, silent=True)

        if not data:
            return "Data must be in JSON format", 404
        try:
            meetup_id = len(all_meetups) + 1
            location = data['location']
            topic = data['topic']

            meetup_record = Meetups().create_meetup(meetup_id,location, topic)

            if meetup_record:
                response = jsonify({"status": 201,
                                    "data": meetup_record})
                response.status_code = 201

                return response
            else:
                return 'Could not create meetup', 400

        except:
            return "PLease include all details", 400

    def get(self):
        '''Endpoint for geting all meetup records'''

        meetups = Meetups().get_all_meetups()
        if meetups:
            response = jsonify({"status": 200,
                                "data": meetups})
            response.status_code = 200
            return response
        return {"message": "No meetup found"}


class SingleMeetupApi(Resource):
    '''Endpoint for single meetup functionality'''

    def get(self, meetup_id):
        meetup_available = Meetups().get_one_meetup(meetup_id)
        rsvp_available = [
            rsvp for rsvp in all_rsvps if rsvp['meetup_id'] == meetup_id
        ]
        if meetup_available:
            return {'Meetup': meetup_available,
                    'RSVPs': rsvp_available}, 200
        return {"message": "Meetup not found"}, 404

    def post(self, meetup_id):
        '''Post an RSVP'''

        try:
            data = request.get_json()
            status = data['status']
        except:
            return 'Check input data', 400

        meetup_available = Meetups().get_one_meetup(meetup_id)
        print(meetup_available)
        if not meetup_available:
            return "You cannot RSVP an unavailable meetup", 400

        new_rsvp = Meetups().create_rsvp(meetup_id, status)

        if not new_rsvp:
            return {"Message": 'RSVP could not be saved'}, 400

        return {"Message": 'RSVP saved for meetup {} successfully'.format(meetup_id)}, 201



