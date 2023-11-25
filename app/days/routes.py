from app.days import bp
from flask import request, jsonify
from app.users.routes import User


@bp.route('/')
def index():
    return "Days"


@bp.route('/getInfo')
def get():
    day = request.args.get('day')
    users = User.query.filter_by(id=day).all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])


@bp.route('/postAnswer', methods=["POST"])
def post():
    data = request.get_json()
    return data