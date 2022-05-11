from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this1sKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models




