from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
  
app =   Flask(__name__)
api =   Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class TextbookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Textbook(name = {name}, author = {author}, price = {price})"

textbook_put_args = reqparse.RequestParser()
textbook_put_args.add_argument("name", type=str, help="Textbook name required", required = True)
textbook_put_args.add_argument("price", type=float, help="Textbook price required", required = True)
textbook_put_args.add_argument("author", type=str, help="Textbook author required", required = True)
  
resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'author' : fields.String,
    'price' : fields.Float
}

class ShoppingCart(Resource): # note to self: run main.py in a separate split terminal before running requests in other files, otherwise there will be errors
    @marshal_with(resource_fields)
    def get(self, textbook_id):
        result = TextbookModel.query.filter_by(id=textbook_id).first()
        if not result:
            abort(404, message="Textbook does not exist")
        return result
    
    @marshal_with(resource_fields)
    def put(self, textbook_id):
        args = textbook_put_args.parse_args()
        result = TextbookModel.query.filter_by(id=textbook_id).first()
        if result:
            abort(409, message="Textbook ID is already taken")

        textbook = TextbookModel(id=textbook_id, 
                                 name=args['name'], 
                                 author=args['author'], 
                                 price=args['price'])
        db.session.add(textbook)
        db.session.commit()
        return textbook, 201
    
    def delete(self, textbook_id):
        result = TextbookModel.query.filter_by(id=textbook_id).first()
        if not result:
            abort(404, message="Textbook does not exist")
        db.session.delete(result)
        db.session.commit()
        return '', 204
  
api.add_resource(ShoppingCart,'/shoppingcart/<int:textbook_id>')
  
  
if __name__=='__main__':
    app.run(debug=True)


