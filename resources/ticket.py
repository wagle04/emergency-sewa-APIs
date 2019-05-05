from flask_restful import Resource, reqparse
from models.ticket import TicketModel


class TicketGenerate(Resource):

    generateparser = reqparse.RequestParser()
    generateparser.add_argument('user_id',
                            type=int,
                            required=True,
                            help='User Id cannot be blank!')

    generateparser.add_argument('agent_id',
                            type=int,
                            default=None)

    generateparser.add_argument('type',
                            type=str,
                            required=True,
                            help='Type cannot be blank!')

    generateparser.add_argument('time_created',
                            type=str,
                            required=True,
                            help='Time Created cannot be blank!')

    generateparser.add_argument('time_solved',
                            type=str,
                            default=None)

    generateparser.add_argument('user_confirm',
                            type=bool,
                            default=False)
    
    generateparser.add_argument('agent_confirm',
                            type=bool,
                            default=False)
    
    generateparser.add_argument('solved',
                            type=bool,
                            default=False)


    def post(self):
        data = TicketGenerate.generateparser.parse_args()

        ticket = TicketModel(**data)
        try:
            ticket_id = ticket.save_to_db()
        except:
            return {"message": "An error occured while generating ticket"}, 500  

        

        return {"message": "Ticket generated successfully", "ticket_id":ticket_id}, 201


class TicketInfo(Resource):

    infoparser = reqparse.RequestParser()
    infoparser.add_argument('ticket_id',
                            type=str,
                            required=True,
                            help='Ticket Id cannot be blank!')

    def post(self):
        data = TicketInfo.infoparser.parse_args()
        ticket = TicketModel.find_by_ticketid(data['ticket_id'])
        if ticket:
            return {"message": "Ticket Found", "ticket": ticket.json() }, 200

        return {"message": "Error while searching for ticket"}, 500

class TicketUpdate(Resource):
    
    updateparser = reqparse.RequestParser()

    updateparser.add_argument('ticket_id',
                            type=int,
                            required=True,
                            help='Ticket id cannot be blank!')
                            
    updateparser.add_argument('user_id',
                            type=int,
                            required=True,
                            help='User Id cannot be blank!')

    updateparser.add_argument('agent_id',
                            type=int,
                            default=None)

    updateparser.add_argument('type',
                            type=str,
                            required=True,
                            help='Type cannot be blank!')

    updateparser.add_argument('time_created',
                            type=str,
                            required=True,
                            help='Time Created cannot be blank!')

    updateparser.add_argument('time_solved',
                            type=str,
                            default=None)

    updateparser.add_argument('user_confirm',
                            type=bool,
                            default=False)
    
    updateparser.add_argument('agent_confirm',
                            type=bool,
                            default=False)
    
    updateparser.add_argument('solved',
                            type=bool,
                            default=False)

    def put(self):
        data = TicketUpdate.updateparser.parse_args()

        ticket = TicketModel.find_by_ticketid(data['ticket_id'])
        ticket.user_id = data['user_id']
        ticket.agent_id = data['agent_id']
        ticket.type = data['type']
        ticket.time_created = data['time_created']
        ticket.time_solved = data['time_solved']
        ticket.user_confirm = data['user_confirm']
        ticket.agent_confirm = data['agent_confirm']
        ticket.solved = data['solved']


        try:
            ticket.save_to_db()
        except:
            return {"message": "An error occured updating information of the ticket"}, 500  

        return {"message": "Ticket information updated successfully"}, 201

'''class AgentDelete(Resource):

    deleteparser = reqparse.RequestParser()
    deleteparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')


    def delete(self):
        data = AgentDelete.deleteparser.parse_args()
        agent = AgentModel.find_by_username(data['username'])
        if agent:
            agent.delete_from_db()
        return {'message': 'Agent deleted'}'''
