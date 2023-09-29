from flask import Flask, request
from flask_restful import Api, Resource
from database import db
from database import User


app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(debug=True) 

#class User(Resource):
 #   def get(self):
  #      return {'data': 'Hello World'}
   # 
    #def post(self):
     #   return {'data': 'Posted'}
    
#api.add_resource(User, '/helloworld')

#creating new user
#@app.route('user', methods=['POST'])
def add_user():
    name = request.json['name']
    username = request.json['username']
    password = request.json['password']
    email = request.json['email', None]
    cc_number = request.json['credit card', None]
    home_address = request.json['home address', None]

    new_user = User(name, username, password, email, cc_number, home_address)

    db.session.add(new_user)
    db.session.commit()

BASE = "http://127.0.0.1:5000/"

response = request.post(BASE + "user")
print(response.status_code)
print(response.json())
    
    

