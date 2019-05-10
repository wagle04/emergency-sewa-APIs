from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):

    registerparser = reqparse.RequestParser()
    registerparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')

    registerparser.add_argument('password',
                            type=str,
                            required=True,
                            help='Password cannot be blank!')

    registerparser.add_argument('fname',
                            type=str,
                            required=True,
                            help='First Name cannot be blank!')

    registerparser.add_argument('mname',
                            type=str)

    registerparser.add_argument('lname',
                            type=str,
                            required=True,
                            help='Last Name cannot be blank!')

    registerparser.add_argument('phone_number',
                            type=str,
                            required=True,
                            help='Phone Number cannot be blank!')

    registerparser.add_argument('date_of_birth',
                            type=str,
                            required=True,
                            help='Date of Birth cannot be blank!')

    registerparser.add_argument('email',
                            type=str,
                            required=True,
                            help='Email cannot be blank!')

    registerparser.add_argument('assist',
                            type=str,
                            required=True,
                            help='Assist cannot be blank!')

    registerparser.add_argument('personal_id',
                            type=str,
                            required=True,
                            help='Personal Identification cannot be blank!')

    def post(self):
        data = UserRegister.registerparser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 409

        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
            return {"message": "An error occured registering user"}, 500  

        return {"message": "User created successfully"}, 201



class UserLogin(Resource):

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
        data = UserLogin.loginparser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            return {"message": "Login Success", "user": user.json() }, 200

        return {"message": "Invalid username or password !"}, 401


class UserUpdate(Resource):

    updateparser = reqparse.RequestParser()
    updateparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')

    updateparser.add_argument('password',
                            type=str,
                            required=True,
                            help='Password cannot be blank!')

    updateparser.add_argument('fname',
                            type=str,
                            required=True,
                            help='First Name cannot be blank!')

    updateparser.add_argument('mname',
                            type=str)

    updateparser.add_argument('lname',
                            type=str,
                            required=True,
                            help='Last Name cannot be blank!')

    updateparser.add_argument('phone_number',
                            type=str,
                            required=True,
                            help='Phone Number cannot be blank!')

    updateparser.add_argument('date_of_birth',
                            type=str,
                            required=True,
                            help='Date of Birth cannot be blank!')

    updateparser.add_argument('email',
                            type=str,
                            required=True,
                            help='Email cannot be blank!')

    updateparser.add_argument('assist',
                            type=str,
                            required=True,
                            help='Assist cannot be blank!')

    updateparser.add_argument('personal_id',
                            type=str,
                            required=True,
                            help='Personal Identification cannot be blank!')

    def put(self):
        data = UserUpdate.updateparser.parse_args()

        user = UserModel.find_by_username(data['username'])
        user.password = data['password']
        user.fname = data['fname']
        user.mname = data['mname']
        user.lname = data['lname']
        user.phone_number = data['phone_number']
        user.date_of_birth = data['date_of_birth']
        user.email = data['email']
        user.assist = data['assist']
        user.personal_id = data['personal_id']

        try:
            user.save_to_db()
        except:
            return {"message": "An error occured updating information of  user"}, 500  

        return {"message": "User information updated successfully"}, 201

class UserDelete(Resource):

    deleteparser = reqparse.RequestParser()
    deleteparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')


    def delete(self):
        data = UserDelete.deleteparser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            user.delete_from_db()
        return {'message': 'User deleted'}

    
