"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, User, Message, Follows

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"


# Now we can import app

from app import app, do_login, do_logout, signup

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

    
    def test_repr_work(self):
        u = User(
            id=1,
            email='test@test.com',
            username='testuser',
            password='HASHED_PASSWORD'
        )
        db.session.add(u)
        db.session.commit()

        self.assertEqual(u.__repr__(), "<User #1: testuser, test@test.com>")

    
    def test_is_following(self):
        u1 = User(
            id=1,
            email='test@test.com',
            username='testuser',
            password='HASHED_PASSWORD'
        )
        db.session.add(u1)
        db.session.commit()

        u2 = User(
            id=2,
            email='test2@test.com',
            username='testuser2',
            password='HASHED_PASSWORD'
        )
        db.session.add(u2)
        db.session.commit()

        f = Follows(
            user_being_followed_id=1,
            user_following_id=2
        )
        db.session.add(f)
        db.session.commit()

        self.assertEqual(u2.is_following(u1), True)
        self.assertFalse(u1.is_following(u2))


    def test_is_followed_by(self):
        u1 = User(
            id=1,
            email='test@test.com',
            username='testuser',
            password='HASHED_PASSWORD'
        )
        db.session.add(u1)
        db.session.commit()

        u2 = User(
            id=2,
            email='test2@test.com',
            username='testuser2',
            password='HASHED_PASSWORD'
        )
        db.session.add(u2)
        db.session.commit()

        f = Follows(
            user_being_followed_id=1,
            user_following_id=2
        )
        db.session.add(f)
        db.session.commit()

        self.assertEqual(u1.is_followed_by(u2), True)
        self.assertFalse(u2.is_followed_by(u1))


    def test_signup_creates_new_user_with_valid_credentials(self):
        self.testuser = User.signup(username="testuser",
                                    email="test@test.com",
                                    password="testuser",
                                    image_url=None)

        db.session.commit()

        self.assertEqual(len(User.query.all()), 1)

    
    
        

     
        

           

        

    
        



        




        
        

    
    
        

       
        



