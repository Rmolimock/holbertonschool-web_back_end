#!/usr/bin/env python3
"""
Before request and error handling
"""
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views
from flask_cors import (CORS, cross_origin)
from os import getenv
import os


# instantiate the app, add cors protection, and check which authentication
# method it should run with.
app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = os.getenv("AUTH_TYPE")
if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
elif auth_type == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
elif auth_type == "session_db_auth":
    from api.v1.auth.session_db_auth import SessionDBAuth
    auth = SessionDBAuth()
else:
    pass


@app.before_request
def before():
    """
    Authenticate and set current user
    """
    if auth:
        if not auth.require_auth(
                            request.path,
                            ['/api/v1/status/',
                             '/api/v1/unauthorized/',
                             '/api/v1/forbidden/',
                             '/api/v1/auth_session/login/']):
            return
        if not auth.authorization_header(request):
            if not auth.session_cookie(request):
                abort(401)
        if auth.current_user(request):
            request.current_user = auth.current_user(request)
        else:
            abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def Forbidden(error) -> str:
    """ Forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def Unauthorized(error) -> str:
    """ Unauthorized
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    """ entry point """
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
