from flask import Flask, request, jsonify
from flask_restful import Resource
from app.api.v1.models.meetupsmodel import all_meetups, Meetups


class AllMeetupsApi(Resource):
    '''Endpoint for all meetups functionality'''
    def get(self):
        '''Endpoint for geting all meetup records'''

        meetups = Meetups().get_all_meetups()
        # print(all_meetups)
        response = jsonify({"status": 200,
                            "data": meetups})
        response.status_code = 200
        return response

    def post(self):
        data = request.get_json()

        if not data:
            return "Data must be in JSON format", 404
        try:
            meetup_id = len(all_meetups) + 1
            location = data["location"]
            topic = data["topic"]

            meetup_record = Meetups().create_meetup(meetup_id,
                                                    location, topic)
            print(all_meetups)
            print(meetup_record)

            if meetup_record:
                response = jsonify({"status": 201,
                                    "data": meetup_record})
                response.status_code = 201
                print(all_meetups)
                return response
            else:
                return 'Could not create meetup', 400

        except Exception as e:
            return "PLease include all details", 400
           