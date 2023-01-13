import os
from unittest import TestCase
from app import app
from models import db, User, Message, Follows

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

db.drop_all()
db.create_all()

class MessageModelTestCase(TestCase):
    """Test for message model"""

    def setUp(self):
        """Clean up any existing messages"""

        Message.query.delete()

    def tearDown(self):

        db.session.rollback()

    def test_message_model(self):

        test_user = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(test_user)
        db.session.commit()
        
        msg = Message(
            text="Testingtesting", 
            user_id=f"{test_user.id}"
        )

        db.session.add(msg)
        db.session.commit()

        self.assertEqual(len(test_user.messages), 1)

