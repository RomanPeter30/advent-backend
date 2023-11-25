from app.extensions import db


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    text = db.Column(db.String(1000))
    image = db.Column(db.BLOB(800000))
    options = db.relationship('Option')


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.BLOB(800000))
    text = db.Column(db.String(300))
    correct = db.Column(db.Boolean)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))
