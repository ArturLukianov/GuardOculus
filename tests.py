from datetime import datetime, timedelta
import unittest
from app import db, create_app
from app.models import User, Location, Camera, MapObject

from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DB_URI = "sqlite://"

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

if __name__ == "__main__":
    unittest.main(verbosity=2)