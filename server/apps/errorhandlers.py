

from flask import request, render_template, jsonify

def init_errorhandlers(app):
    @app.errorhandler(404)
    def error_404(error):
      if request.path[:5] == '/api/':
        return jsonify({
            "ok": False,
            "error": 404,
            "message": "Not Found"
            }), 404
      return "NOT FOUND", 404


