#!/usr/bin/env python3
''' app.py '''

from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
