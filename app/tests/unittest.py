import pytest
import unittest,os
from app import app, db
from app.models import User, Stats, Puzzle

class UserModelCase(unittest.TestCase):

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'test.db')
        self.app = app.test_client()
        db.create_all()
        user1 = User(id='1', username='hello', email='123@gmail.com')
        user2 = User(id='2', username='hey', email='456@gmail.com')
        user3 = User(id='3', username='hi', email='789@gmail.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.commit()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        user1 = User.query.get('1')
        user1.set_password('test')
        self.assertFalse(user1.check_password('case'))
        self.assertTrue(user1.check_password('test'))

    
    