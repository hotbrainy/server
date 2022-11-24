import json
from secrets import token_hex
from flask import request, jsonify, abort, flash, make_response,redirect, render_template, Blueprint, url_for
from server.db.models import User
from server.apps.auth import AuthError
from server.tools.mail_sender import send_email_verification
from email_validator import validate_email, caching_resolver, EmailNotValidError
from flask_mail import Message, Mail
from server.tools.token import generate_confirmation_token, confirm_token
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, \
                               unset_jwt_cookies, jwt_required, JWTManager, create_refresh_token, current_user
from flask_restful import Resource, Api, fields, marshal_with

resolver = caching_resolver(timeout=10)
mail = Mail()


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
            try:
                email = validate_email(email, dns_resolver=resolver).email
            except EmailNotValidError as e:
                print(e)
                raise AuthError("The email address is not valid. It must have exactly one @-sign.", 400)

            user = User.query.filter_by(email=email).first()

            if user:
                raise AuthError("User already exists.", 409)

            new_User = User(
                email=email,
                password=data.get('password'),
                first_name=data.get('first_name')
            )
            new_User.insert() 
            # send_email_verification(mail, email)
            token = generate_confirmation_token(email)
            confirm_url = url_for('confirmtoken', token=token, _external=True)
            html = render_template('user/activate.html', confirm_url=confirm_url)
            subject = "Please confirm your email"
            send_email_verification(email, subject, html, mail)
            return api_response({
                "external_id": new_User.external_id,
                "email": new_User.email
            }, "Created successfully.", 201
            )
        except AuthError as s: raise s
        # except: abort(400)

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


class ConfirmToken(Resource):
    @jwt_required()
    def get(self):
        if current_user.confirmed:
            flash('Account already confirmed. Please login.', 'success')
            return api_response(current_user.get_all(short=True), "Got user details.")
        email = confirm_token(token)
        user = User.query.filter_by(email=current_user.email).first_or_404()
        if user.email == email:
            user.confirmed = True
            user.confirmed_on = datetime.datetime.now()
            db.session.add(user)
            db.session.commit()
            flash('You have confirmed your account. Thanks!', 'success')
        else:
            flash('The confirmation link is invalid or has expired.', 'danger')
        return api_response(current_user.get_all(short=True), "Got user details.")



def init_rest_api(app):
    # This function is connected to app
    

    api = Api(app)
    mail.init_app(app)

    api.add_resource(LoginResource, '/api/login')
    api.add_resource(SignUpResource, '/api/signup')
    api.add_resource(RefreshResource, '/api/refresh')
    api.add_resource(WhoAmIResource, '/api/whoami')
    api.add_resource(ConfirmToken, '/api/confirmtoken')


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


