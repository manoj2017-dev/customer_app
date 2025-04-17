from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from .models import load_user

mongo = PyMongo()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app

@login_manager.user_loader
def user_loader(user_id):
    return load_user(user_id)
