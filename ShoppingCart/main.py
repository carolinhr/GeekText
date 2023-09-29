from flask import Flask
from flask_restful import Api, Resource
  
app =   Flask(__name__)
api =   Api(app)

names = {"textbook": {"price": 70.00, "vol": 2},
         "textbook2": {"price": 60.00, "vol": 1},
         "textbook3": {"price": 65.00, "vol": 3}}
  
class ShoppingCart(Resource): # note to self: run main.py in a separate split terminal before running requests in other files, otherwise there will be errors
    def get(self, name):
        return names[name]
  
api.add_resource(ShoppingCart,'/shoppingcart/<string:name>')
  
  
if __name__=='__main__':
    app.run(debug=True)


