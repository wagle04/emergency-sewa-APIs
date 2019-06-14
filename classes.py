from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()



class Admins(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone_number = db.Column(db.String(10))
    date_of_birth = db.Column(db.String(50))
    email = db.Column(db.String(50))


class Agent(db.Model):
    __tablename__ = 'agents'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    phone_number = db.Column(db.String(10))
    vehicle_no = db.Column(db.String(50))
    availability = db.Column(db.Boolean)
    type = db.Column(db.String(50))

class AgentLocations(db.Model):
    __tablename__ = 'agentlocations'

    agent_id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

class Ticket(db.Model):
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
    valid = db.Column(db.Boolean)
    

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(100))
    fname = db.Column(db.String(50))
    mname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    phone_number = db.Column(db.String(10))
    date_of_birth = db.Column(db.String(50))
    email = db.Column(db.String(50))
    assist = db.Column(db.String(50))
    personal_id = db.Column(db.String(100000))


class UserLocations(db.Model):
    __tablename__ = 'userlocations'

    user_id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

class UserView(ModelView):
    column_display_pk = True
    can_create = False
    column_exclude_list = ('password', 'personal_id')
    column_searchable_list = ('username', 'email','id','fname','assist')
    column_labels = dict(fname='First Name', lname='Last Name', mname='Middle Name')
    edit_modal = True

 

class AgentView(ModelView):
    column_display_pk = True
    can_create = True
    column_exclude_list = ('password')
    column_searchable_list = ('username', 'availability','type')
    create_modal = True
    edit_modal = True

class AdminsView(ModelView):
    column_display_pk = True
    can_create = True
    column_exclude_list = ('password')
    column_searchable_list = ('username', 'email')
    column_labels = dict(fname='First Name', lname='Last Name', mname='Middle Name')
    create_modal = True
    edit_modal = True

class UserLocationView(ModelView):
    column_display_pk = True
    can_create = True
    column_searchable_list = ('')
    create_modal = True
    edit_modal = True
    
class AgentLocationView(ModelView):
    column_display_pk = True
    can_create = True
    column_searchable_list = ('')
    create_modal = True
    edit_modal = True

class TicketView(ModelView):
    column_display_pk = True
    can_create = True
    column_searchable_list = ('')
    create_modal = True
    edit_modal = True


