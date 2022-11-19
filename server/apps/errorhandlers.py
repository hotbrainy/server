
from flask import jsonify
from flask_jwt_extended import JWTManager

def init_app_errorhandlers(app):
    # This function is connected to app

    from server.apps.auth import AuthError

    @app.errorhandler(404)
    def error_404(error):
        return jsonify({
            "ok": False,
            "error_code": 404,
            "description": "Not Found"
            }), 404

    @app.errorhandler(405)
    def error_405(error):
        return jsonify({
            "ok": False,
            "error_code": 405,
            "description": "Method Not Allowed. The method is not allowed for the requested URL"
            }), 405
    
    @app.errorhandler(AuthError)
    def error_auth_errors(error):
        return jsonify({
            "ok": False,
            "error_code": error.error_code,
            "description": error.description
        }), error.error_code
    


def init_jwt_errorhandlers(jwt:JWTManager):
    pass



