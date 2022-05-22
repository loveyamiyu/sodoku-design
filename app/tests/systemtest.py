import unittest,os,time
from selenium import webdriver
from app import app, db
from app.models import User, Stats

class SystemTest(unittest.TestCase):
    driver = None

    def setup(self):
        self.driver = webdriver.Firefox(executable_path=''
        )

        if not self.driver:
            self.skpiTest('Web browser not available')
        
        else:
            db.init_app(app)
            db.create_all
            # create 3 users as test cases
            user1 = User(username='hello', email='123@gmail.com')
            user2 = User(username='hey', email='456@gmail.com')
            user3 = User(username='hi', email='789@gmail.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
            db.session.commit()
            self.driver.maximize_window()
            self.driver.get('http://localhost:5000')

    def tearDown(self):
        # remove all the db data so the test can be reusable
        if self.driver:
            db.session.query(User).delete()
            db.session.commit
            db.session.remove()
    
    def test_register(self):
        user1 = User.query.filter_by(username='hello')
        self.assertEqual(user1.email,'123@gmail.com',msg="this user is registered")
        
