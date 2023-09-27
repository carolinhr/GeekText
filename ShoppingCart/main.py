from flask import Flask
from flask_restful import Api, Resource
  
app =   Flask(__name__)
api =   Api(app)
  
class ShoppingCart(Resource): # note to self: run main.py & open up the host address on browser before running API requests, otherwise there will be errors
    def get(self):
        return {"name": "Textbook1",
                "price": "$60.00",
                "description": "Textbook1 Description"
                }
    
    def post(self):
        return {"name": "Textbook2",
                "price": "$70.00",
                "description": "Textbook2 Description"
                }
  
api.add_resource(ShoppingCart,'/shoppingcart')
  
  
if __name__=='__main__':
    app.run(debug=True)


