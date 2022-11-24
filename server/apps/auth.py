from server.db.models import User
from server.tools.mail_sender import send_email_verification



from flask_jwt_extended import (JWTManager as JWTManager,
                                create_access_token,create_refresh_token,
                                get_jwt_identity,
                                jwt_required, current_user
                                )
from flask import Flask, request, make_response, abort, g
import logging
from functools import wraps
from server.apps.errorhandlers import init_jwt_errorhandlers

# AuthError Exception
class AuthError(Exception):
    def __init__(self, description, error_code):
        self.description = description
        self.error_code = error_code


def requires_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "id" not in g.cookie:
            logging.warning("No authorization provided!")
            abort(401)
        g.user = User.query.get(g.cookie["id"])
        if not g.user:
            response = make_response("", 401)
            response.set_cookie("user", "")
            return response
        return func(*args, **kwargs)
    return wrapper


def init_api_authentication(app):
    # This function is connected to app

    from server.apps.api import Jsonify

    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(external_id=identity).one_or_none()


    # init_jwt_errorhandlers(jwt)

