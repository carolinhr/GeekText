from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
  
app =   Flask(__name__)
api =   Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class TextbookModel(db.Model):
    __tablename__ = 'textbook'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Textbook(name = {name}, author = {author}, price = {price})"

textbook_post_args = reqparse.RequestParser()
textbook_post_args.add_argument("name", type=str, help="Textbook name required", required = True)
textbook_post_args.add_argument("price", type=float, help="Textbook price required", required = True)
textbook_post_args.add_argument("author", type=str, help="Textbook author required", required = True)

  
resource_fields = {
    'id' : fields.Integer,
    'user_id' : fields.Integer,
    'name' : fields.String,
    'author' : fields.String,
    'price' : fields.Float
}

class ShoppingCart(Resource): # note to self: run main.py in a separate split terminal before running requests in other files, otherwise there will be errors
    @marshal_with(resource_fields)
    def get(self, user_id):
        textbooks = TextbookModel.query.filter_by(user_id=user_id).all()
        if not textbooks:
            abort(404, message="Shopping cart empty.")
        textbook_list = [{"id": textbook.id, "name": textbook.name, "author": textbook.author, "price": textbook.price} for textbook in textbooks]
        return textbook_list
    
    @marshal_with(resource_fields)
    def post(self, user_id):
        args = textbook_post_args.parse_args()
        new_textbook = TextbookModel(user_id=user_id,
                                 name=args['name'],
                                 author=args['author'], 
                                 price=args['price'])
        db.session.add(new_textbook)
        db.session.commit()
        return {"message": "Textbook added successfully."}, 201
  
class Textbook(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id, textbook_id):
        textbook_to_get = TextbookModel.query.filter_by(id=textbook_id, user_id=user_id).first()
        if not textbook_to_get:
            abort(404, message="Textbook does not exist.")
        return textbook_to_get
    
    @marshal_with(resource_fields)
    def delete(self, user_id, textbook_id):
        textbook_to_delete = TextbookModel.query.filter_by(id=textbook_id, user_id=user_id).first()
        if not textbook_to_delete:
             abort(404, message="Textbook does not exist.")
        db.session.delete(textbook_to_delete)
        db.session.commit()
        return {"message": f"Textbook with ID {textbook_id} has been deleted."}, 204
        

api.add_resource(ShoppingCart,'/shoppingcart/<int:user_id>')
api.add_resource(Textbook,'/shoppingcart/<int:user_id>/<int:textbook_id>')
  
if __name__=='__main__':
    app.run(debug=True)