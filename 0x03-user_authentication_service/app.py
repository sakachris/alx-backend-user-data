#!/usr/bin/env python3
''' app.py '''

from flask import Flask, jsonify, request, abort
from auth import Auth
from typing import Dict, Any

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome() -> str:
    ''' welcome '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> Dict[str, Any]:
    ''' endpoint to register user '''
    try:
        email: str = request.form.get('email')
        password: str = request.form.get('password')

        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> Dict[str, Any]:
    ''' endpoint to log in user '''
    email: str = request.form.get('email')
    password: str = request.form.get('password')

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response, 200
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")