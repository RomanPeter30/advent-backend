import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))


def __init__(self, name):
    self.name = name


@app.route('/')
def index():  # put application's code here
    users = User.query.all()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run()
