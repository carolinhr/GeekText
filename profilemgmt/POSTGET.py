from flask import Flask, request, jsonify, Blueprint
from flask_restful import Api, Resource
from database import User, db, CC

postget_routes = Blueprint('postget_routes', __name__)

#creating new user
@postget_routes.route('/user', methods=['POST'])
def add_user():
    data = request.json
    username = data['username']
    password = data['password']
    name = data['name']
    email = data.get('email') # use .get() to handle missing keys 
    credit_card = data.get('credit_card') 
    home_address = data.get('home_address')

    # create a new User object and add it to the database
    new_user = User(username, password, name, email, home_address, credit_card)
    db.session.add(new_user)
    db.session.commit()
    return 'User added successfully', 201  # return a success response
   

@postget_routes.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        user_data = {
            'username': user.username,
            'name': user.name,
            'password': user.password,
            'email': user.email,
            'home_address': user.home_address,
        }
        if user.credit_card:
            user_data['credit card'] = {
                'number': user.credit_card.cc_number,
                'cvv': user.credit_card.cvv,
                'expiration date': user.credit_card.expiration_date
            }
        return jsonify(user_data), 200
    else:
        return 'User not found', 404
    
