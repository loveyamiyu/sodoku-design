
import pytest
import unittest,os
from app import app, db
from app.models import User, Stats, Puzzle
from app.forms import RegistrationForm, LoginForm

class UserModelCase(unittest.TestCase):

    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'test.db')
        self.app = app.test_client() # create a vitual test enviroment
        db.create_all()
        # create 3 users as test cases
        user1 = User(username='hello', email='123@gmail.com')
        user2 = User(username='hey', email='456@gmail.com')
        user3 = User(username='hi', email='789@gmail.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.add(user3)
        db.session.commit()

        self.assertEquals(app.debug, False)

    def tearDown(self):
        # remove all the db data so the test can be reusable
        db.session.remove() 
        db.drop_all()

    def test_password_hashing(self):
        user1 = User.query.filter_by(username='hello')
        user1.set_password('testhello')
        self.assertFalse(user1.check_password('casehello'))
        self.assertTrue(user1.check_password('testhello'))
    
    def register(self,username,email,password,confirm):
        return self.app.post('signup/', 
            data=dict(username=username,email=email, password=password, confirm=confirm),
            follow_redirects=True)

    def test_user_registration_form_displays(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)

    def test_valid_user_registration(self):
        self.app.get('/signup', follow_redirects=True)
        response = self.register('hello', '123@gmail.com', 'IHateFlask', 'IHateFlask')
        self.assertIn(b'', response.data)

    def test_registration_different_passwords(self):
        response = self.register('hello', '123@gmail.com', 'IHateFlask', 'ILoveFlask')
        self.assertIn(b'Field must be equal to password.', response.data)

    def test_registration_duplicate_email(self):
        response = self.register('yes', '123@gmail.com', 'IHateFlask', 'IHateFlask')
        self.assertEqual(response.status_code, 200)
        response = self.register('no', '123@gmail.com', 'IHateFlask', 'IHateFlask')
        self.assertIn(b'Username taken, please pick a different one', response.data)
    
    def test_registration_duplicate_username(self):
        self.app.get('/signup', follow_redirects=True)
        self.register('hello', '456@gmail.com', 'IHateFlask', 'IHateFlask')
        self.app.get('/signup', follow_redirects=True)
        response = self.register('hello', '123@gmail.com', 'IHateFlask', 'IHateFlask')
        self.assertIn(b'Email already in use, please try a different one or reset password', response.data)
    
    def login(self, username, password):
        return self.app.post('/login',
            data=dict(username=username, password=password),
            follow_redirects=True)

    def test_login_form_displays(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)

    def test_valid_user_login(self):
        self.app.get('/login', follow_redirects=True)
        response = self.login('hello', 'IHateFlask')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'', response.data)
    
    def test_login_wrong_username(self):
        self.app.get('/login', follow_redirects=True)
        response = self.login('hell', 'IHateFlask')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid username', response.data)
    
    def test_login_wrong_password(self):
        self.app.get('/login', follow_redirects=True)
        response = self.login('hello', 'ILoveFlask')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid password', response.data)

    def test_valid_logout(self):
        self.app.get('/register', follow_redirects=True)
        self.register('hello', '123@gmail.com', 'IHateFlask', 'IHateFlask')
        self.app.get('/login', follow_redirects=True)
        self.login('hello', 'IHateFlask')
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'', response.data)
        
    def test_invalid_logout_within_being_logged_in(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'', response.data)

if __name__ == "__main__":
    unittest.main()
    
    