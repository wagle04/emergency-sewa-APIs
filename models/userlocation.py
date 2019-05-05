import sqlite3
from db import db

class UserLocationModel(db.Model):
    __tablename__ = 'userlocations'

    user_id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    def __init__(self, user_id, longitude, latitude):
        self.user_id = user_id
        self.longitude = longitude
        self.latitude = latitude

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'user_id': self.user_id,'longitude':self.longitude, 'latitude':self.latitude}

    @classmethod
    def find_by_userid(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
