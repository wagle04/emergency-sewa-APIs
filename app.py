import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister, UserLogin, UserUpdate, UserDelete
from resources.admin import AdminRegister, AdminLogin, AdminUpdate, AdminDelete
from resources.agent import AgentRegister, AgentLogin, AgentUpdate, AgentDelete

app = Flask(__name__)
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

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=3000, debug=True)
