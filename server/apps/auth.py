
from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort, redirect, url_for, session, request, jsonify
from flask_wtf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mail import Mail
from server.db.forms import LoginForm
from server.db.models import User

# AuthError Exception
class AuthError(Exception):
    def __init__(self, description, status_code):
        self.description = description
        self.status_code = status_code


def init_api_authentication(app):
    # This function is connected to app
    login_manager = LoginManager()
    login_manager.login_view = 'not_logged_in'
    login_manager.init_app(app)
    csrf = CSRFProtect(app)
    mail = Mail(app)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    @app.route("/api/@me")
    def rest_api_get_current_user():
        user_token_id = session.get("user_token_id")

        if not user_token_id:
            raise AuthError("Unauthorized", 401)
        
        user = User.query.filter_by(token_id=user_token_id).first()

        return jsonify({
            "ok": True,
            "result": {
                "token_id": user.id,
                "email": user.email
            }
        }) 

    @app.route("/api/register", methods=["POST"])
    def rest_api_register_user():
        try:
            email = request.json["email"]
            password = request.json["password"]
            first_name = request.json["first_name"]

            user = User.query.filter_by(email=email).first()

            if not user:
                return jsonify({"ok": False, "error_code": 409,  "description": "User already exists"}), 409
            
            new_User = User(first_name=first_name, email=email, password=generate_password_hash(password, method='sha256'))
            new_User.insert()
            
            session["user_token_id"] = new_User.token_id
            
            return jsonify({
                "ok": True,
                "result": {
                    "token_id": new_User.id,
                    "email": new_User.email
                }
            })
        except:
            abort(400)
    
    @app.route("/api/login", methods=["POST"])
    def rest_api_login_user():
        try:
            email = request.json["email"]
            password = request.json["password"]

            user = User.query.filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password):
                raise AuthError("Unauthorized", 401)
            
            session["user_token_id"] = user.token_id

            return jsonify({
                "ok": True,
                "result": {
                    "token_id": user.id,
                    "email": user.email
                }
            })

        except: abort(400)
    

    @app.route("/api/logout", methods=["GET"])
    def rest_api_logout_user():
        user_token_id = session["user_token_id"] 
        session.pop("user_token_id")
        return jsonify({
            "ok": True,
            "result": {
                "token_id": user_token_id
            }
        })


