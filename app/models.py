from datetime import datetime
from typing_extensions import Self
from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model): #subclass user

    id = db.Column(db.Integer, primary_key=True) # Each user has only one unique id;
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True) 
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.set_password(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


#needs revision 
class Stats(db.Model): # subclass stats used to store the results of users
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, nullable=False) 
    puzzle = db.Column(db.JSON, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Reference to user id in user table

    def __repr__(self):
        return "[Username:{},Time spend:{}]".format(self.user_id,self.time)
    
    # Read users from database
    def get_user():
        return  User.query.filter_by().all()

# Puzzle class 

class Puzzle(db.Model): # may not use the model as we can save puzzle into the stats model
    id = db.Column(db.Integer, primary_key=True) #puzzle id
    puzzle = db.Column((db.Integer), db.ForeignKey('puzzle'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False) 



def init_db():
    db.drop_all()
    db.create_all()

    # Create a test user
    new_user = User()
    new_user.display_name = 'Nathan'
    db.session.add(new_user)
    db.session.commit()



if __name__ == '__main__':
    init_db()
