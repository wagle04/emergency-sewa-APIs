import sqlite3
from db import db

class AgentLocationModel(db.Model):
    __tablename__ = 'agentlocations'

    agent_id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    def __init__(self, agent_id, longitude, latitude):
        self.agent_id = agent_id
        self.longitude = longitude
        self.latitude = latitude

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {'agent_id': self.agent_id,'longitude':self.longitude, 'latitude':self.latitude}

    @classmethod
    def find_by_agentid(cls, agent_id):
        return cls.query.filter_by(agent_id=agent_id).first()
