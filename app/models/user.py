from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    points = db.Column(db.Integer)
    tookPart = db.Column(db.Integer)


