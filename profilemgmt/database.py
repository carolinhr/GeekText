from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, render_template, request, session, flash
import os

db = SQLAlchemy()


class User(db.Model):
    username = db.Column(db.String, unique = True, nullable = False, primary_key = True) 
    password = db.Column(db.String, nullable = False)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)
    home_address = db.Column('home address', db.String)
    credit_card = db.relationship('CC', backref='user', uselist=False)

    def __init__(self, username, password, name, email, home_address, credit_card):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.home_address = home_address
        self.credit_card = credit_card

class CC(db.Model):
    username = db.Column(db.String, db.ForeignKey('user.username'), nullable=False, primary_key = True)
    cc_number = db.Column('credit card number', db.String(16), nullable = False)
    cvv = db.Column(db.String, nullable = False)
    expiration_date = db.Column('expiration date', db.String, nullable = False)

    def __init__(self, username, cc_number, cvv, expiration_date):
        self.username = username
        self.cc_number = cc_number
        self.cvv = cvv
        self.expiration_date = expiration_date
       
        

