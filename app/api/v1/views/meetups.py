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