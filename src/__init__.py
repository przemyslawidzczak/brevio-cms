from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = os.getenv('DB_SECRET')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
    db.init_app(app)

    

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from views.users import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app