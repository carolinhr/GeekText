#new databse info pending
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
db = SQLAlchemy(app)

Base = declarative_base()


class User:
    id int
    username str
    email str



