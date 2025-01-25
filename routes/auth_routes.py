# src/routes/auth_routes.py

from flask import Blueprint, request, jsonify
# flask_jwt_extended é modulo para instalar
from flask_jwt_extended import create_access_token
from models.person import Person
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = Person.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.idperson)
        return jsonify({"token": access_token}), 200

    return jsonify({"message": "Invalid credentials"}), 401
