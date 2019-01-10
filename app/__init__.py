from flask import Flask, Blueprint
from flask_restful import Api, Resource
from instance.config import app_config


def create_app(config_name):
    '''load the right configurations from config.py given a config name'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config["development"])

    '''Import and register the blueprint from the factory'''
    from app.api.v1 import app_v1
    app.register_blueprint(app_v1)

    return app