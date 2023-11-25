import json

from app.days import bp
from flask import request, jsonify, Response

from app.models.day import Day
from app.models.user import User
from app.models.overview import Overview
from app.extensions import db

@bp.route('/')
def index():
    return "Days"


@bp.route('/getInfo')
def get():
    day = request.args.get('day')
    dayInfo = Day.query.filter_by(id=day).first()

    #Nicht schön, am Besten iterativ über Optionen gehen, Probleme mit jsonify
    option1 = dayInfo.options[0]
    option2 = dayInfo.options[1]
    option3 = dayInfo.options[2]
    return jsonify([{"id": dayInfo.id, "text": dayInfo.text, "image": dayInfo.image, "option1":
        {"id": option1.id, "text": option1.text, "correct": option1.correct}, "option2": {"id": option2.id, "text": option2.text, "correct": option2.correct}, "option3": {"id": option3.id, "text": option3.text, "correct": option3.correct}}])


@bp.route('/postAnswer', methods=["POST"])
def post():
    request_data = request.get_json()

    user = User.query.filter_by(name=request_data['user']).first()
    dayInfo = Day.query.filter_by(day=request_data['day']).first()
    givenAnswer = request_data['answer']

    if dayInfo.options[givenAnswer].correct:
        user.points += 1
        user.tookPart += 1
        db.session.add(user)
        db.session.commit()
        print(user.points)
    else:
        user.tookPart += 1
        db.session.add(user)
        db.session.commit()

    return jsonify([{"id": user.id, "name": user.name, "text": dayInfo.text}])