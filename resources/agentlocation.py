from flask_restful import Resource, reqparse
from models.agentlocation import AgentLocationModel


class AgentLocation(Resource):

    updateparser = reqparse.RequestParser()
    updateparser.add_argument('agent_id',
                            type=int,
                            required=True,
                            help='Agent Id cannot be blank!')

    updateparser.add_argument('longitude',
                            type=float,
                            required=True,
                            help='Longitude cannot be blank')

    updateparser.add_argument('latitude',
                            type=float,
                            required=True,
                            help='Latitude cannot be blank!')



    def post(self):
        data = AgentLocation.updateparser.parse_args()

        agentlocation = AgentLocationModel(**data)
        try:
            agentlocation.save_to_db()
        except:
            return {"message": "An error occured while updating location of agent"}, 500  

        return {"message": "Location of agent created successfully"}, 201


class AgentLocationInfo(Resource):

    infoparser = reqparse.RequestParser()
    infoparser.add_argument('agent_id',
                            type=str,
                            required=True,
                            help='Agent Id cannot be blank!')

    def post(self):
        data = AgentLocationInfo.infoparser.parse_args()
        agent_location = AgentLocationModel.find_by_agentid(data['agent_id'])
        if agent_location:
            return {"agent_location_info": agent_location.json() }, 200

        return {"message": "Error while searching for agent location"}, 500

class AgentLocationUpdate(Resource):
    
    updateparser = reqparse.RequestParser()
    updateparser.add_argument('agent_id',
                            type=int,
                            required=True,
                            help='Agent Id cannot be blank!')

    updateparser.add_argument('longitude',
                            type=float,
                            required=True,
                            help='Longitude cannot be blank')

    updateparser.add_argument('latitude',
                            type=float,
                            required=True,
                            help='Latitude cannot be blank!')

    def put(self):
        data = AgentLocationUpdate.updateparser.parse_args()

        agent = AgentLocationModel.find_by_agentid(data['agent_id'])
        agent.agent_id = data['agent_id']
        agent.longitude = data['longitude']
        agent.latitude = data['latitude']


        try:
            agent.save_to_db()
        except:
            return {"message": "An error occured updating location of agent"}, 500  

        return {"message": "Location of agent updated successfully"}, 201

