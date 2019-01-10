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

    def test_get_one_meetup(self):
        '''Test if the user can get a specific meetup record'''
        response = self.client.get(
            'api/v1/meetups/1', content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_create_meetup(self):
        '''Test if admin can create a meetup'''
        response = self.client.post(
            'api/v1/meetups', data=json.dumps(self.data), content_type="application/json")
        self.assertEqual(response.status_code, 201)