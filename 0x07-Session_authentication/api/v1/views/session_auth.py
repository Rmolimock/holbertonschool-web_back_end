#!/usr/bin/env python3
""" routes for session authentication """

from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def user_login():
    """ validate email and password """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({"email": email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    for each in user:
        if not each:
            return jsonify({"error": "no user found for this email"}), 404
        if not each.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 404
        from api.v1.app import auth
        session_id = auth.create_session(each.id)
        response = jsonify(each.to_json())
        response.set_cookie(getenv("SESSION_NAME"), session_id)
        return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def user_logout():
    """ destroy current session to log out the user """
    from api.v1.app import auth
    logout = auth.destroy_session(request)
    if logout:
        return jsonify({}), 200
    abort(404)
