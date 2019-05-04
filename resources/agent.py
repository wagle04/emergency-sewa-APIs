from flask_restful import Resource, reqparse
from models.agent import AgentModel


class AgentRegister(Resource):

    registerparser = reqparse.RequestParser()
    registerparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')

    registerparser.add_argument('password',
                            type=str,
                            required=True,
                            help='Password cannot be blank!')


    registerparser.add_argument('phone_number',
                            type=int,
                            required=True,
                            help='Phone Number cannot be blank!')

    registerparser.add_argument('vehicle_no',
                            type=str,
                            required=True,
                            help='Vehicle no cannot be blank!')

    registerparser.add_argument('availability',
                            type=bool,
                            required=True,
                            help='Availability cannot be blank!')

    registerparser.add_argument('type',
                            type=str,
                            required=True,
                            help='Type cannot be blank!')

    def post(self):
        data = AgentRegister.registerparser.parse_args()

        if AgentModel.find_by_username(data['username']):
            return {"message": "An agent with that username already exists"}, 409

        agent = AgentModel(**data)
        try:
            agent.save_to_db()
        except:
            return {"message": "An error occured registering agent"}, 500  

        return {"message": "Agent created successfully"}, 201


class AgentLogin(Resource):

    loginparser = reqparse.RequestParser()
    loginparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')

    loginparser.add_argument('password',
                            type=str,
                            required=True,
                            help='Password cannot be blank!')
    def post(self):
        data = AgentLogin.loginparser.parse_args()
        agent = AgentModel.find_by_username(data['username'])
        if agent:
            return {"message": "Login Success", "agent": agent.json() }, 200

        return {"message": "Invalid username or password !"}, 401

class AgentUpdate(Resource):
    
    updateparser = reqparse.RequestParser()
    updateparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')

    updateparser.add_argument('password',
                            type=str,
                            required=True,
                            help='Password cannot be blank!')

    updateparser.add_argument('phone_number',
                            type=int,
                            required=True,
                            help='Phone Number cannot be blank!')

    updateparser.add_argument('vehicle_no',
                            type=str,
                            required=True,
                            help='Vehicle no cannot be blank!')

    updateparser.add_argument('availability',
                            type=bool,
                            required=True,
                            help='Availability cannot be blank!')

    updateparser.add_argument('type',
                            type=str,
                            required=True,
                            help='Type cannot be blank!')

    def put(self):
        data = AgentUpdate.updateparser.parse_args()

        agent = AgentModel.find_by_username(data['username'])
        agent.password = data['password']
        agent.phone_number = data['phone_number']
        agent.vehicle_no = data['vehicle_no']
        agent.availability = data['availability']
        agent.type = data['type']

        try:
            agent.save_to_db()
        except:
            return {"message": "An error occured updating information of  agent"}, 500  

        return {"message": "Agent information updated successfully"}, 201

class AgentDelete(Resource):

    deleteparser = reqparse.RequestParser()
    deleteparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')

    deleteparser.add_argument('password',
                            type=str,
                            required=True,
                            help='Password cannot be blank!')

    def delete(self):
        data = AgentDelete.deleteparser.parse_args()
        agent = AgentModel.find_by_username(data['username'])
        if agent:
            agent.delete_from_db()
        return {'message': 'Agent deleted'}
