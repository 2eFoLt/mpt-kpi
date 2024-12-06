from flask import Blueprint, jsonify, request, url_for
from flask_login import login_user, logout_user
from flask_mail import Message

from .builder import db, mail
from .models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        login_user(user)
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

@auth_bp.route("/reset_password", methods=["POST"])
def reset_password():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    token = user.id  # Using ID as an example token
    reset_url = url_for("auth.complete_reset", token=token, _external=True)

    msg = Message("Password Reset Request", recipients=[user.email])
    msg.body = f"To reset your password, visit the following link: {reset_url}"
    mail.send(msg)

    return jsonify({"message": "Reset link sent"}), 200

@auth_bp.route("/reset_password/<token>", methods=["POST"])
def complete_reset(token):
    user = User.query.get(int(token))
    if not user:
        return jsonify({"error": "Invalid token"}), 400

    data = request.json
    user.set_password(data["password"])
    db.session.commit()
    return jsonify({"message": "Password reset successful"}), 200
