from app.extensions import db


class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    image = db.Column(db.String(300))
    options = db.relationship('Option')


class Option(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300))
    correct = db.Column(db.Boolean)
