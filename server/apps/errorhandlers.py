
from server.apps.auth import AuthError
from flask import request, render_template, jsonify


def init_errorhandlers(app):
  
  
    @app.errorhandler(404)
    def error_404(error):
      # if request.path[:5] == '/api/':
        return jsonify({
            "ok": False,
            "error_code": 404,
            "description": "Not Found"
            }), 404
      # return "NOT FOUND", 404


    @app.errorhandler(AuthError)
    def error_auth_errors(error):
        return jsonify({
          "ok": False,
          "error_code": error.error_code,
          "description": error.description
        }), error.error_code
    
