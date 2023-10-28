from flask import Flask, request, jsonify, Blueprint
from flask_restful import Api, Resource
from database import User, db

patch_routes = Blueprint('patch_routes', __name__)

@patch_routes.route('/user/<username>', methods=['PATCH'])
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
