from app.models.user import User
from app.users import bp
from flask import jsonify


@bp.route('/')
def index():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "points": u.points, "tookPart": u.tookPart} for u in users])