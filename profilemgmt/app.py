from flask import Flask, request, jsonify, Blueprint
from flask_restful import Api, Resource
from PATCH import patch_routes
from POSTGET import postget_routes
from database import db
import os

app = Flask(__name__)
#api = Api(app)

app.register_blueprint(patch_routes)
app.register_blueprint(postget_routes)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
app.run(debug=True)