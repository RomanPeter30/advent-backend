from app.extensions import db

db.drop_all()
db.create_all()
