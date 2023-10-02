from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from database import *

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Set to False to disable tracking

db.init_app(app)

#creating new user
@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    username = data['username']
    password = data['password']
    name = data['name']
    email = data.get('email') # use .get() to handle missing keys 
    cc_number = data.get('credit_card') 
    home_address = data.get('home_address')

    # Create a new User object and add it to the database
    new_user = User(username, password, name, email, cc_number, home_address)
    db.session.add(new_user)
    db.session.commit()
    return 'User added successfully', 201  # return a success response
   

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        # Convert the User object to a dictionary for JSON serialization
        user_data = {
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'credit_card': user.cc_number,
            'home_address': user.home_address
        }
        return jsonify(user_data), 200
    else:
        return 'User not found', 404
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
app.run(debug=True)
    

