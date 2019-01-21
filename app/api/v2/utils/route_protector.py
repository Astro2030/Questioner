"""define custom decorators for routes"""
from functools import wraps
from flask import request, jsonify, make_response
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from os import getenv


def admin_required(f):
    """decorator for admin protected routes"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        identity = get_jwt_identity()
        if identity != getenv('admin'):
            return make_response(jsonify({
                'message': 'Forbidden. You are not an Admin'
            }), 403)
        else:
            return f(*args, **kwargs)
    return wrapper
