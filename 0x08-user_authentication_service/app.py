#!/usr/bin/env python3

from flask import Flask, jsonify, request, abort
from db import DB
from auth import Auth

app = Flask(__name__)
db = DB()
auth = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ basic route """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ register users """
    email, password = request.form.get('email'), request.form.get('password')
    try:
        auth.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"}), 200
    except Exception as e:
        # print(e)
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ route for user login """
    email, password = request.form.get('email'), request.form.get('password')
    if auth.valid_login(email, password):
        session_id = auth.create_session(email)
        response = jsonify({"email": f"{email}", "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """ route for logging out a user """
    session = request.cookies.get('session_id')
    user = auth.get_user_from_session_id(session)
    if not user:
        abort(403)
    else:
        auth.destroy_session(user.id)
        return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """ route for getting info about a user (email) """
    session = request.cookies.get('session_id')
    user = auth.get_user_from_session_id(session)
    if not user:
        abort(403)
    else:
        return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """ request a reset token from the server
        - this function mimics what would actually be a message
        - to the customer email address
    """
    email = request.form.get('email')
    user = auth.create_session(email)
    if not user:
        abort(403)
    else:
        reset_token = auth.get_reset_password_token(email)
        return jsonify({"email": f"{email}", "reset_token": f"{reset_token}"})


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """ pass back reset token (exercise) """
    email = request.form.get('email')
    new_password = request.form.get('new_password')
    reset_token = request.form.get('reset_token')
    if not email or not new_password or not reset_token:
        abort(403)
    try:
        auth.update_password(reset_token, new_password)
        return jsonify({"email": f"{email}",
                        "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
