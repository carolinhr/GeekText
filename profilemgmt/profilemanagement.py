
from flask import Flask, request
from flask_restful import Api, Resource
import sys
sys.path.append('/Users/carolinheredia/GeekText/database.py')
from database import db


from database import db

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self):
        return {'data': 'Hello World'}
    
    def post(self):
        return {'data': 'Posted'}
    
api.add_resource(User, '/helloworld')

#creating new user
@app.route('/user', methods=['POST'])
def add_user():
    name = request.json['name']
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    cc_number = request.json['credit card']
    home_address = request.json['home address']

    new_user = User(name, username, password, email, cc_number, home_address)

    db.session.add(new_user)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True) 
