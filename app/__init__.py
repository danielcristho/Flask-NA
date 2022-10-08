from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from app import routes

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interface.db'
db = SQLAlchemy(app)