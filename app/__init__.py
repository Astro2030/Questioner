'''Application entry module'''
from flask import Flask,jsonify
from flask_jwt_extended import JWTManager

from app.api import AUTH_BLUEPRINT, API_BLUEPRINT
from app.api.v2.models.db import reg_app
from instance.config import APP_CONFIG

def create_app(config_name):
    '''Instantiate the Flask application'''
    app = Flask(__name__, instance_relative_config=True)
    jwt = JWTManager(app)
    app.config.from_object(APP_CONFIG["development"])
    app.config.from_pyfile('config.py')
    reg_app(app)
    app.register_blueprint(AUTH_BLUEPRINT)
    app.register_blueprint(API_BLUEPRINT)

    return app

