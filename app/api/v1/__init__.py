from flask import Blueprint
from flask_restful import Api
from app.api.v1.views.meetups import AllMeetupsApi


# create variable called api_v1 that defines the blueprint and registers it in the application factory
app_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')
api_v1 = Api(app_v1)

api_v1.add_resource(AllMeetupsApi, '/meetups/upcoming')
