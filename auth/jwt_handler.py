# src/auth/jwt_handler.py

import jwt
from datetime import datetime, timedelta
from flask import current_app

def create_token(person):
    payload = {
        'id': person.idperson,
        'exp': datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def decode_token(token):
    try:
        return jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None