import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone_number = db.Column(db.Integer)
    date_of_birth = db.Column(db.String(50))
    email = db.Column(db.String(50))
    assist = db.Column(db.String(50))
    personal_id = db.Column(db.String(100000))

    def __init__(self, username, password, fname, mname, lname, phone_number,date_of_birth, email, assist, personal_id):
        self.username = username
        self.password = password
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.email = email
        self.assist = assist
        self.personal_id = personal_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'username': self.username,'password':self.password, 'fname':self.fname, 'mname':self.mname,'lname':self.lname,'phone_number':self.phone_number,'date_of_birth':self.date_of_birth,'email':self.email,'assist':self.assist,'personal_id':self.personal_id}


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
