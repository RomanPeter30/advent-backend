from flask import Flask
from app.extensions import db
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.days import bp as days_bp
    app.register_blueprint(days_bp, url_prefix='/days')

    return app
