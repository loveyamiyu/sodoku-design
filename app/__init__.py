from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'this1sKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'tests/test.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'

from app import routes, models, forms

if __name__ == "__main__":
    app.run(debug=True)




