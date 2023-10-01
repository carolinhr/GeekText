from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, render_template, request, session, flash
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite') #real URI TBD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    #_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable= False, primary_key = True) #need for having username as primary key TBD
    password = db.Column(db.String, nullable= False)
    name = db.Column(db.String)
    email = db.Column(db.String)
    cc_number = db.Column('card number', db.Integer)
    home_address = db.Column('home address', db.String)
    
    def __init__(self, username, password, name, email, cc_number, home_address):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.cc_number = cc_number
        self.home_address = home_address

if __name__ == "__main__":
    app.run(debug=True)
#create new classes based on chosen features (ex: book genres, prices, etc.)