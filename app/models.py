from datetime import datetime
from app import db
from app import login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % self.username

#needs revision 
class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    difficulty = db.Column(db.String(140))
    time = db.Column(db.Integer) 
    startTime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    finishTime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Stats {}>'.format(self.body)