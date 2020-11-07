#!/usr/bin/env python3
"""
routes
"""
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
if os.getenv("AUTH_TYPE") == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
else:
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before():
    """ check request
    """
    if auth:
        if auth.require_auth(
                            request.path,
                            ['/api/v1/status/',
                             '/api/v1/unauthorized/',
                             '/api/v1/forbidden/']):
            if not auth.authorization_header(request):
                abort(401)
            if not auth.current_user(request):
                abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ not found
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def Forbidden(error) -> str:
    """ forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def Unauthorized(error) -> str:
    """ unauthorized
    """
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    """ main """
    from os import getenv
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
