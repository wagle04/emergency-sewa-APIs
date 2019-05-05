from flask_restful import Resource, reqparse
from models.admin import AdminModel


class AdminRegister(Resource):

    
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
                            type=int,
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

    def post(self):
        data = AdminRegister.registerparser.parse_args()

        if AdminModel.find_by_username(data['username']):
            return {"message": "An admin with that username already exists"}, 409

        admin = AdminModel(**data)
        try:
            admin.save_to_db()
        except:
            return {"message": "An error occured registering admin"}, 500  

        return {"message": "Admin created successfully"}, 201


class AdminLogin(Resource):

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
        data = AdminLogin.loginparser.parse_args()
        admin = AdminModel.find_by_username(data['username'])
        if admin:
            return {"message": "Login Success", "admin": admin.json() }, 200

        return {"message": "Invalid username or password !"}, 401

    
    
class AdminUpdate(Resource):

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
                            type=int,
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

    def put(self):
        data = AdminUpdate.updateparser.parse_args()

        admin = AdminModel.find_by_username(data['username'])
        admin.password = data['password']
        admin.fname = data['fname']
        admin.mname = data['mname']
        admin.lname = data['lname']
        admin.phone_number = data['phone_number']
        admin.date_of_birth = data['date_of_birth']
        admin.email = data['email']

        try:
            admin.save_to_db()
        except:
            return {"message": "An error occured updating information of  admin"}, 500  

        return {"message": "Admin information updated successfully"}, 201

class AdminDelete(Resource):

    deleteparser = reqparse.RequestParser()
    deleteparser.add_argument('username',
                            type=str,
                            required=True,
                            help='Username cannot be blank!')

    def delete(self):
        data = AdminDelete.deleteparser.parse_args()
        admin = AdminModel.find_by_username(data['username'])
        if admin:
            admin.delete_from_db()
        return {'message': 'Admin deleted'}
