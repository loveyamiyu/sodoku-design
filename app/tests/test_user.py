import pytest
import unittest
from app import app, db

class FormCase(unittest.TestCase):
    def test_user_registration_form_displays(self):
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please Register Your New Account', response.data)

    def test_valid_user_registration(self):
        self.app.get('/signup', follow_redirects=True)
        response = self.register('hello', '123@gmail.com', 'IHateFlask', 'IHateFlask')
        self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thanks for registering!', response.data)

    def test_registration_different_passwords(self):
        self.app.get('/signup', follow_redirects=True)
        response = self.register('hello', '123@gmail.com', 'IHateFlask', 'ILoveFlask')
        self.app.get('/register', follow_redirects=True)
        self.assertIn(b'Field must be equal to password.', response.data)

    def test_registration_duplicate_email(self):
        response = self.register('yes', '123@gmail.com', 'IHateFlask', 'IHateFlask')
        self.app.get('/signup', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username already registered', response.data)
    
    def test_registration_duplicate_username(self):
        self.app.get('/signup', follow_redirects=True)
        response = self.register('hello', '456@gmail.com', 'IHateFlask', 'IHateFlask')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Email already registered', response.data)

    def test_login_form_displays(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In', response.data)

    def test_valid_user_login(self):
        self.app.get('/login', follow_redirects=True)
        response = self.login('hello', 'IHateFlask')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'You\'re logged in', response.data)
    
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
        self.assertIn(b'Goodbye!', response.data)
        
    def test_invalid_logout_within_being_logged_in(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'Log In', response.data)