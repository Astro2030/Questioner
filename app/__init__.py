'''Application entry module'''
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from app.api.v2 import AUTH_BLUEPRINT, API_BLUEPRINT
from app.api.v2.models.db import reg_app
from instance.config import APP_CONFIG

def create_app():
    '''Instantiate the Flask application'''
    app = Flask(__name__, instance_relative_config=True)
    jwt = JWTManager(app)

    @app.errorhandler(404)
    def not_found(e):
        """custom error handler for 404 Not Found Error"""
        return jsonify({
            "error": "Not Found. Please refer to the API documentation"
        }), 404

    @app.errorhandler(500)
    def server_error(e):
        """custom error handler for 500 Internal Sever Error"""
        app.logger.error('An error occured', e)
        return jsonify({
            "error": "An error occured. Please try again later"
        }), 500

    @app.errorhandler(405)
    def not_implemented(e):
        """custom error handler for 405 Not Implemented Error"""
        return jsonify({
            "error": "Method not implemented. Refer to the API documentation"
        }), 405

    @jwt.expired_token_loader
    def my_expired_token_callback():
        return jsonify({
            'status': 401,
            'msg': 'The token has expired'
        }), 401

    app.config.from_object(APP_CONFIG["development"])
    app.config.from_pyfile('config.py')
    reg_app(app)
    app.register_blueprint(AUTH_BLUEPRINT)
    app.register_blueprint(API_BLUEPRINT)

    return app
