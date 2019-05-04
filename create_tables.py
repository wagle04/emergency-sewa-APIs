import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text, fname text, mname text, lname text, phone_number INTEGER, date_of_birth text, email text, assist text, personal_id text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS admins(id INTEGER PRIMARY KEY, username text, password text, fname text, mname text, lname text, phone_number INTEGER, date_of_birth text, email text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS agents(id INTEGER PRIMARY KEY, username text, password text, phone_number INTEGER, vehicle_no text, availability boolean, type text)"
cursor.execute(create_table)

connection.commit()
connection.close()