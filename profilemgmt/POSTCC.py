from flask import Flask, request, jsonify, Blueprint
from flask_restful import Api, Resource
from database import User, db, CC

postcc_routes = Blueprint('postcc_routes', __name__)

@postcc_routes.route('/addcc/<username>', methods=['POST'])
def add_cc(username):
    data = request.json #to access user fields in its json format
    user = User.query.filter_by(username=username).one_or_none()
    if user is None:
        return 'User does not exist', 404
    
    if 'credit card number' not in data or 'cvv' not in data or 'expiration date' not in data:
        return 'Incomplete credit card information', 400        
    
    credit_card = CC(username=username, cc_number=data['credit card number'], cvv=data['cvv'], expiration_date=data['expiration date'])

    existing_credit_card = CC.query.filter_by(username=username, cc_number=data['credit card number']).first()

    if existing_credit_card is not None:
        return 'Credit card already added', 400

    db.session.add(credit_card)
    db.session.commit() #commit changes to database
    return 'Credit card added successfully', 200