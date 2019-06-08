import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister, UserLogin, UserUpdate, UserDelete
from resources.admin import AdminRegister, AdminLogin, AdminUpdate, AdminDelete
from resources.agent import AgentRegister, AgentLogin, AgentUpdate, AgentDelete
from resources.ticket import TicketGenerate, TicketInfo, TicketUpdate
from resources.userlocation import UserLocation, UserLocationInfo, UserLocationUpdate
from resources.agentlocation import AgentLocation, AgentLocationInfo, AgentLocationUpdate

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///G:\\Projects\\py programs\\web interface for emergency sewa\\data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sewa'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/userregister')
api.add_resource(UserLogin, '/userlogin')
api.add_resource(UserUpdate, '/userupdate')
api.add_resource(UserDelete, '/userdelete')

api.add_resource(AdminRegister, '/adminregister')
api.add_resource(AdminLogin, '/adminlogin')
api.add_resource(AdminUpdate, '/adminupdate')
api.add_resource(AdminDelete, '/admindelete')

api.add_resource(AgentRegister, '/agentregister')
api.add_resource(AgentLogin, '/agentlogin')
api.add_resource(AgentUpdate, '/agentupdate')
api.add_resource(AgentDelete, '/agentdelete')

api.add_resource(TicketGenerate, '/ticketgenerate')
api.add_resource(TicketInfo, '/ticketinfo')
api.add_resource(TicketUpdate, '/ticketupdate')

api.add_resource(UserLocation, '/userlocation')
api.add_resource(UserLocationInfo, '/userlocationinfo')
api.add_resource(UserLocationUpdate, '/userlocationupdate')

api.add_resource(AgentLocation, '/agentlocation')
api.add_resource(AgentLocationInfo, '/agentlocationinfo')
api.add_resource(AgentLocationUpdate, '/agentlocationupdate')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=3000, debug=True)
