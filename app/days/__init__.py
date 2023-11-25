from flask import Blueprint

bp = Blueprint('days', __name__)

from app.days import routes