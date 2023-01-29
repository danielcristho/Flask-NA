from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

"""
App & Config, DB, Encryption
"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = '7d1ce04a2ba2b81c2a566a04'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

"""
Login manager stuff
"""
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from app import routes
