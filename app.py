import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister, UserLogin, UserUpdate, UserDelete, UserExist
from resources.admin import AdminRegister, AdminLogin, AdminUpdate, AdminDelete
from resources.agent import AgentRegister, AgentLogin, AgentUpdate, AgentDelete
from resources.ticket import TicketGenerate, TicketInfo, TicketUpdate
from resources.userlocation import UserLocation, UserLocationInfo, UserLocationUpdate
from resources.agentlocation import AgentLocation, AgentLocationInfo, AgentLocationUpdate
from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask_admin import Admin,expose,BaseView, AdminIndexView
from flask_bootstrap import Bootstrap
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from classes import User, Agent, Admins, UserLocations, AgentLocations, Ticket
from classes import UserView, AgentView, AdminsView, UserLocationView, AgentLocationView, TicketView
import json
import requests
from functools import wraps
import sqlite3

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///G:\\Projects\\py programs\\web interface for emergency sewa\\data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'Simplex'
app.secret_key = 'sewa'

api = Api(app)
db = SQLAlchemy(app)
Bootstrap(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/userregister')
api.add_resource(UserLogin, '/userlogin')
api.add_resource(UserUpdate, '/userupdate')
api.add_resource(UserDelete, '/userdelete')
api.add_resource(UserExist, '/userexist')

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


@app.route('/')
def home():
    return render_template('index.html')


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


class DashboardView(BaseView):
    @expose('/')
    def index(self):
        conn = sqlite3.connect('data.db')
        c=conn.cursor()
        c.execute('select * from tickets')
        tickets=list(c.fetchall())

        conn.close()
        session['tickets']=tickets

        return redirect(url_for('dashboard'))



admin = Admin(app, name='Emergency Sewa Databases', template_mode='bootstrap3')

admin.add_view(DashboardView(name='Dashboard'))
admin.add_view(UserView(User, db.session))
admin.add_view(AgentView(Agent, db.session))
admin.add_view(AdminsView(Admins, db.session))
admin.add_view(UserLocationView(UserLocations, db.session))
admin.add_view(AgentLocationView(AgentLocations, db.session))
admin.add_view(TicketView(Ticket, db.session))






@app.route('/viewlocation/<tid>')
def viewlocation(tid):
    conn = sqlite3.connect('data.db')
    c=conn.cursor()
    c.execute('select user_id, agent_id,type from tickets where ticket_id=?',tid)
    ids=list(c.fetchall())
    user_id=ids[0][0]
    agent_id=ids[0][1]
    types=ids[0][2]
    c.execute('select  latitude,longitude from userlocations where user_id=?',[user_id])
    user_location=list(c.fetchall())
    c.execute('select  latitude,longitude from agentlocations where agent_id=?',[agent_id])
    agent_location=list(c.fetchall())
    return render_template('viewlocation.html',agent_location=agent_location,user_location=user_location,user=user_id,agent=agent_id,types=types)


@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password_candiate = request.form['password']
        api_url = 'http://wagle04.pythonanywhere.com/adminlogin'
        headers = {'Content-Type': 'application/json'}
        body = {'username':username,'password': password_candiate}

        response = requests.post(api_url, data=body)


        if response.status_code == 200:
            
            #connection to get data from database about tickets
            conn = sqlite3.connect('data.db')
            c=conn.cursor()
            c.execute('select * from tickets')
            tickets=list(c.fetchall())

            conn.close()

            #code for successfull login and setting up session variables
            data = response.json()
            session['logged_in'] = True
            session['username']=data['admin']['username']
            session['fname']=data['admin']['fname']
            session['mname']=data['admin']['mname']
            session['lname']=data['admin']['lname']
            session['phone_number']=data['admin']['phone_number']
            session['date_of_birth']=data['admin']['date_of_birth']
            session['email']=data['admin']['email']
            session['tickets']=tickets
            flash('Login Successful','success')
            return render_template('dashboard.html')#redirect('http://127.0.0.1:5000/dashboard')
        
        else:
            flash ('Invalid username or password','warning')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard', methods=["GET","POST"])
@is_logged_in
def dashboard():
    return render_template('dashboard.html')




@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    flash("You  are now logged out", 'success')
    return redirect(url_for('login'))



if __name__ == '__main__':
   
    app.run(port=3000, debug=True)
