from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

user_password = [
    {
        "username": "Maria",
        "name": "Maria",
        "password_hash": generate_password_hash("passwordmaria")
    },
    {
        "username": "jane",
        "name": "Jane",
        "password_hash": generate_password_hash("passwordjane")
    }
    ]

@HTTPBasicAuth.verify_password
def verify_password(username, password):
    if username in user_password and check_password_hash(user_password.get(username), password):
        return username
