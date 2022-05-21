from datetime import datetime
from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(email):
    return User.query.get(email)

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
        return str(self.email)


#needs revision 
class Stats(db.Model): # subclass stats used to store the results of users
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer) 
    startTime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    finishTime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False) # Reference to user id in user table

"""""

def init_db():
    db.create_all()

    # Create a test user
    new_user = User()
    new_user.display_name = 'Nathan'
    db.session.add(new_user)
    db.session.commit()

    new_user.datetime_subscription_valid_until = datetime.datetime(2019, 1, 1)
    db.session.commit()


if __name__ == '__main__':
    init_db()

    """