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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
