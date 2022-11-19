import json
from secrets import token_hex
from flask import request, jsonify, abort, flash, make_response
from server.db.models import User
from server.apps.auth import AuthError
from flask_mail import Mail
from server.tools.mail_sender import send_email_verification
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager, create_refresh_token, current_user
from flask_restful import Resource, Api, fields, marshal_with




def Jsonify(result : dict, description : str = '', status_code : int = 200,):
    return jsonify({
        "ok": True,
        "description": description,
        "result": result
    }), status_code



def api_response(result : dict, description : str = '', status_code : int = 200,):
    return {
        "ok": True,
        "description": description,
        "result": result
    }, status_code


# When documentation of API is needed, we will uncomment these lines:

# from flask_apispec import marshal_with, doc
# from flask_apispec.views import MethodResource
# from marshmallow import Schema, fields
# class LoginSchema(Schema):
#     email = fields.String()
#     password = fields.String()

# class SignUpSchema(Schema):
#     email = fields.String()
#     password = fields.String()
#     first_name = fields.String()
#     phone_number = fields.String()
#     last_name = fields.String()


# change
login_fields = {
    'email': fields.String,
    'password': fields.String
}


signup_fields = {
    'email': fields.String,
    'password': fields.String,
    'first_name': fields.String
}


class LoginResource(Resource):
    def post(self, **kwargs):
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')

            db_user = User.query.filter_by(email=email, is_confirmed=True).first()
            if not db_user:
                raise AuthError("Login details are invalid.", 401)
            if not db_user.verify_password(password):
                raise AuthError("Login details are invalid.", 401)
            
            access_token = create_access_token(identity=db_user.external_id)
            refresh_token = create_refresh_token(identity=db_user.external_id)

            return api_response({
                "access_token": access_token,
                "refresh_token": refresh_token
                }, "Logged in successfully")
            
        except: abort(400)



class SignUpResource(Resource):
    def post(self):
        try:
            data = request.get_json()

            email = data.get('email')

            user = User.query.filter_by(email=email).first()

            if user:
                raise AuthError("User already exists.", 409)

            new_User = User(
                email=email,
                password=data.get('password'),
                first_name=data.get('first_name')
            )
            new_User.insert()
            
            # send_email_verification(mail, email )
            return api_response({
                "external_id": new_User.external_id,
                "email": new_User.email
            }, "Created successfully.", 201
            )
        except AuthError as s: raise s
        except: abort(400)

class RefreshResource(Resource):
    @jwt_required(refresh=True)
    def get(self):
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return api_response({
            "access_token": new_access_token
            })

class WhoAmIResource(Resource):
    @jwt_required()
    def get(self):
        return api_response(current_user.get_all(short=True), "Got user details.")



def init_rest_api(app):
    # This function is connected to app
    

    api = Api(app)


    api.add_resource(LoginResource, '/api/login')
    api.add_resource(SignUpResource, '/api/signup')
    api.add_resource(RefreshResource, '/api/refresh')
    api.add_resource(WhoAmIResource, '/api/whoami')


    @app.route('/api/api')
    def rest_api_index():
        return Jsonify({
            'api_working': True
        },
            "Checking API running."  
        )
    
    # When documentation of API is needed, we will uncomment these lines:

    # from apispec import APISpec
    # from apispec.ext.marshmallow import MarshmallowPlugin
    # from flask_apispec.extension import FlaskApiSpec

    # app.config.update({
    #     'APISPEC_SPEC': APISpec(
    #         title='API Documentation',
    #         version='v1',
    #         plugins=[MarshmallowPlugin()],
    #         openapi_version='2.0.0'
    #     ),
    #     'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    #     'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
    # })
    # docs = FlaskApiSpec(app)

    # docs.register(LoginResource)
    # docs.register(SignUpResource)
    # docs.register(RefreshResource)


