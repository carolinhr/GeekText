from flask import Flask
from flask_restful import Api, Resource
  
app =   Flask(__name__)
api =   Api(app)

names = {"textbook": {"price": 70.00, "vol": 2},
         "textbook2": {"price": 60.00, "vol": 1}}
  
class ShoppingCart(Resource): # note to self: run main.py in a separate split terminal before running requests in other files, otherwise there will be errors
    def get(self, name, test):
        return {"name": name, "test": test}
    
    def post(self):
        return {"name": "Textbook2",
                "price": "$70.00",
                "description": "Textbook2 Description"
                }
  
api.add_resource(ShoppingCart,'/shoppingcart/<string:name>/<int:test>')
  
  
if __name__=='__main__':
    app.run(debug=True)


