from flask import Flask, request
from flask_restful import Api, Resource, abort
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
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class ShoppingCartModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    textbook_id = db.Column(db.Integer, db.ForeignKey('textbook.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    textbook = db.relationship('TextbookModel', backref=db.backref('shopping_cart', lazy=True))

class DummyData(Resource):
    def post(self):
        dummy_items = [
            TextbookModel(name='Biology 101',author='John Doe',price=50.00),
            TextbookModel(name='Anatomy 101',author='Jane Doe',price=60.00),
            TextbookModel(name='Chemistry 101',author='Professor X',price=100.00),
            TextbookModel(name='Driving 101',author='Mrs. Puff',price=40.00),
            TextbookModel(name='Programming 101',author='Steve Jobs',price=70.00),
            TextbookModel(name='Politics 101',author='Barack Obama',price=75.00),
            TextbookModel(name='Writing 101',author='William Shakespeare',price=60.00),
            TextbookModel(name='Art 101',author='Vincent van Gogh',price=65.00),
            TextbookModel(name='Singing 101', author='Taylor Swift',price=50.00),
            TextbookModel(name='Cooking 101',author='Gordon Ramsay',price=45.00)
        ]
        
        db.session.bulk_save_objects(dummy_items)
        db.session.commit()
    
        return {'message': 'Dummy data added successfully.'}, 201
    
    def get(self):
        textbooks=TextbookModel.query.all()
        if not textbooks:
            abort(404, message="No dummy data available.")
        textbook_list = [{"id": textbook.id, 
                          "name": textbook.name, 
                          "author": textbook.author, 
                          "price": textbook.price} for textbook in textbooks]
        return textbook_list

class ShoppingCart(Resource): # note to self: run main.py in a separate split terminal before running requests in other files, otherwise there will be errors
    def get(self, user_id):
        cart_textbooks = (
            db.session.query(ShoppingCartModel, TextbookModel)
            .join(TextbookModel, TextbookModel.id == ShoppingCartModel.textbook_id)
            .filter(ShoppingCartModel.user_id == user_id)
            .all()
        )
        if not cart_textbooks:
            abort(404, message="Shopping cart empty.")

        cart_list = []
        for cart_textbook, textbook in cart_textbooks:
            cart_list.append(
                {
                    "textbook_id": textbook.id, 
                    "name": textbook.name, 
                    "author": textbook.author, 
                    "price": textbook.price, 
                    "quantity": cart_textbook.quantity
                }
            )

        return {'user_id': user_id, 'shopping_cart': cart_list}

  
class Textbook(Resource):
    def post(self, user_id, textbook_id):
        textbook = TextbookModel.query.get_or_404(textbook_id)
        if not textbook:
            abort(404,message="Textbook does not exist.")

        quantity = int(request.args.get('quantity', 1))

        existing_textbook = ShoppingCartModel.query.filter_by(user_id=user_id, textbook_id=textbook_id).first()
        if existing_textbook:
            existing_textbook.quantity += quantity
        else:
            new_textbook = ShoppingCartModel(user_id=user_id, textbook_id=textbook_id, quantity=quantity)
            db.session.add(new_textbook)

        db.session.commit()
        return {"message": "Textbook added successfully."}, 201

    def delete(self, user_id, textbook_id):
        textbook = ShoppingCartModel.query.filter_by(user_id=user_id, textbook_id=textbook_id).first()
        if not textbook:
             abort(404, message="Textbook does not exist.")
        db.session.delete(textbook)
        db.session.commit()
        return {"message": f"Textbook with ID {textbook_id} has been deleted."}, 204

class Subtotal(Resource):
    def get(self, user_id):
        cart_textbooks = (
            db.session.query(ShoppingCartModel, TextbookModel)
            .join(TextbookModel, TextbookModel.id == ShoppingCartModel.textbook_id)
            .filter(ShoppingCartModel.user_id == user_id)
            .all()
        )
        if not cart_textbooks:
            abort(404, message="Shopping cart empty.")

        subtotal = 0

        for cart_textbook, textbook in cart_textbooks:
            subtotal += textbook.price * cart_textbook.quantity
        
        return {'subtotal': subtotal}

api.add_resource(ShoppingCart,'/shoppingcart/<int:user_id>')
api.add_resource(Textbook,'/shoppingcart/<int:user_id>/<int:textbook_id>')
api.add_resource(Subtotal,'/shoppingcart/<int:user_id>/subtotal')
api.add_resource(DummyData,'/shoppingcart/dummydata')
  
if __name__=='__main__':
    app.run(debug=True)