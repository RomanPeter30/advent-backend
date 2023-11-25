from app.extensions import db


class Overview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    day = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    answer = db.Column(db.Integer)
