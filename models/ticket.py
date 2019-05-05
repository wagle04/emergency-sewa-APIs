import sqlite3
from db import db

class TicketModel(db.Model):
    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50))
    agent_id = db.Column(db.String(100))
    type = db.Column(db.String(50))
    time_created = db.Column(db.String(50))
    time_solved = db.Column(db.String(50))
    user_confirm = db.Column(db.Boolean)
    agent_confirm = db.Column(db.Boolean)
    solved = db.Column(db.Boolean)
    


    def __init__(self, user_id, agent_id, type, time_created, time_solved, user_confirm, agent_confirm, solved):
        
        self.user_id = user_id
        self.agent_id = agent_id
        self.type = type
        self.time_created = time_created
        self.time_solved = time_solved
        self.user_confirm = user_confirm
        self.agent_confirm = agent_confirm
        self.solved = solved

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return self.ticket_id

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'ticket_id': self.ticket_id,'user_id':self.user_id, 'agent_id':self.agent_id, 'type':self.type, 'time_created':self.time_created,'time_solved':self.time_solved, 'user_confirm':self.user_confirm, 'agent_confirm':self.agent_confirm ,'solved':self.solved}


    @classmethod
    def find_by_userid(cls, userid):
        return cls.query.filter_by(user_id=userid)

    @classmethod
    def find_by_agentid(cls, agentid):
        return cls.query.filter_by(agent_id=agentid)

    @classmethod
    def find_by_type(cls, type):
        return cls.query.filter_by(type=type)

    @classmethod
    def find_by_ticketid(cls, ticket_id):
        return cls.query.filter_by(ticket_id=ticket_id).first()
