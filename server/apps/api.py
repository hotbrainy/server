import json
from secrets import token_hex
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from flask import request, jsonify, abort, flash, session
from server.db.models import User
from server.apps.auth import AuthError
import os



def init_rest_api(app):
    # This function is connected to app

    @app.route('/api/api')
    def rest_api_index():
        return jsonify({
            "ok": True,
            "result": {
                'api_working': True
            }
        }), 200
    
    @app.route('/api/users')
    def rest_api_users():
        
            users = User.query.all()
            return jsonify({
                "ok": True,
                "result": {
                    "users" : [user.get_all() for user in users]
                }
            }), 200

    