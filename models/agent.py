import sqlite3
from db import db

class AgentModel(db.Model):
    __tablename__ = 'agents'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    phone_number = db.Column(db.String(10))
    vehicle_no = db.Column(db.String(50))
    availability = db.Column(db.Boolean)
    type = db.Column(db.String(50))


    def __init__(self, username, password, phone_number, vehicle_no, availability, type):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.vehicle_no = vehicle_no
        self.availability = availability
        self.type = type

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'username': self.username,'password':self.password, 'phone_number':self.phone_number, 'vehicle_no':self.vehicle_no, 'availability':self.availability,'type':self.type}


    @classmethod
    def find_by_username(cls, username,password):
        return cls.query.filter_by(username=username,password=password).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
