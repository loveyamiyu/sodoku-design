from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
login = LoginManager(app)
db = SQLAlchemy(app)

from app import routes, models