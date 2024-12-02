from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required

from . import db
from .models import Position, User

bp = Blueprint("main", __name__)


@bp.route("/users", methods=["GET", "POST"])
@login_required
def users():
    if request.method == "GET":
        users = User.query.all()
        return jsonify([{"id": u.id, "email": u.email} for u in users])
    elif request.method == "POST":
        if not current_user.is_admin:
            return jsonify({"error": "Access denied"}), 403
        data = request.json
        user = User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created"}), 201


@bp.route("/positions", methods=["GET", "POST"])
@login_required
def positions():
    if not current_user.is_admin:
        return jsonify({"error": "Access denied"}), 403

    if request.method == "GET":
        positions = Position.query.all()
        return jsonify([{"id": p.id, "name": p.name} for p in positions])
    elif request.method == "POST":
        data = request.json
        position = Position(name=data["name"], score_threshold=data["score_threshold"])
        db.session.add(position)
        db.session.commit()
        return jsonify({"message": "Position created"}), 201
