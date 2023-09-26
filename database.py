#new databse info pending
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.config['QLAlchemy_DATABASE_URI'] = 'sqlite:///users.sqlite3' #real URI TBD
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Integer, primary_key = True) #need for having username as primary key TBD
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)
    cc_number = db.Column('card number', db.String(16))
    home_address = db.Column('home address', db.String)
    # add more columns as needed 


