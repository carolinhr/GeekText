from flask import Flask
from flask_restful import Api, Resource
  
app =   Flask(__name__)
api =   Api(app)
  
class returnjson(Resource): # note to self: run main.py & open up the host address on browser before running API requests, otherwise there will be errors
    def get(self):
        return {"data": "Hello World"}
    
    def post(self):
        return {"data": "Posted"}
  
api.add_resource(returnjson,'/returnjson')
  
  
if __name__=='__main__':
    app.run(debug=True)


