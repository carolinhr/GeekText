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
    data = request.json #to access user fields in its json format
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
    data = request.json #to access user fields in its json format
    user = User.query.filter_by(username=username).first()
    if user:
        user_data = {
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'home_address': user.home_address,
            'password' : user.password
        }
        return jsonify(user_data), 200        
    else:
        return 'User not found', 404
    
@app.route('/user/<username>', methods=['PATCH'])
def update_user(username):
    data = request.json #to access user fields in its json format
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return 'User does not exist', 404
    if 'username' in data:
        user.username = data['username']
        db.session.commit() #commit changes to database

    if 'password' in data:
        user.password = data['password']
        db.session.commit() #commit changes to database

    if 'name' in data:
        user.name = data['name']
        db.session.commit() #commit changes to database

    if 'credit_card' in data:
        user.cc_number = data['credit_card']
        db.session.commit() #commit changes to database

    if 'home_address' in data:
        user.home_address = data['home_address']
        db.session.commit() #commit changes to database

    if 'email' in data:
        return 'Unauthorized action: email must not be changed. Any other changes have been updated successfully.', 200
    db.session.commit() #commit changes to database
    return 'User updated successfully', 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
app.run(debug=True)
    

