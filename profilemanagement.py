from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        return {'data': 'Hello World'}
    
    def post(self):
        return {'data': 'Posted'}
    
api.add_resource(Users, '/helloworld')

if __name__ == "__main__":
    app.run(debug=True)