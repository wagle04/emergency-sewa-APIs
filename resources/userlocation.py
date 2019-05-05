from flask_restful import Resource, reqparse
from models.userlocation import UserLocationModel


class UserLocation(Resource):

    updateparser = reqparse.RequestParser()
    updateparser.add_argument('user_id',
                            type=int,
                            required=True,
                            help='User Id cannot be blank!')

    updateparser.add_argument('longitude',
                            type=float,
                            required=True,
                            help='Longitude cannot be blank')

    updateparser.add_argument('latitude',
                            type=float,
                            required=True,
                            help='Latitude cannot be blank!')



    def post(self):
        data = UserLocation.updateparser.parse_args()

        userlocation = UserLocationModel(**data)
        try:
            userlocation.save_to_db()
        except:
            return {"message": "An error occured while updating location of user"}, 500  

        return {"message": "Location of user created successfully"}, 201


class UserLocationInfo(Resource):

    infoparser = reqparse.RequestParser()
    infoparser.add_argument('user_id',
                            type=str,
                            required=True,
                            help='User Id cannot be blank!')

    def post(self):
        data = UserLocationInfo.infoparser.parse_args()
        user_location = UserLocationModel.find_by_userid(data['user_id'])
        if user_location:
            return {"user_location_info": user_location.json() }, 200

        return {"message": "Error while searching for user location"}, 500

class UserLocationUpdate(Resource):
    
    updateparser = reqparse.RequestParser()
    updateparser.add_argument('user_id',
                            type=int,
                            required=True,
                            help='User Id cannot be blank!')

    updateparser.add_argument('longitude',
                            type=float,
                            required=True,
                            help='Longitude cannot be blank')

    updateparser.add_argument('latitude',
                            type=float,
                            required=True,
                            help='Latitude cannot be blank!')

    def put(self):
        data = UserLocationUpdate.updateparser.parse_args()

        user = UserLocationModel.find_by_userid(data['user_id'])
        user.user_id = data['user_id']
        user.longitude = data['longitude']
        user.latitude = data['latitude']


        try:
            user.save_to_db()
        except:
            return {"message": "An error occured updating location of user"}, 500  

        return {"message": "Location of user updated successfully"}, 201

