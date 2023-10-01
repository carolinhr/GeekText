from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

books = {
    "book1": {"Review": "Good", "Rating": 9},
    "book2": {"Review": "Good", "Rating": 8},
    "book3": {"Review": "Bad", "Rating": 1},
}

class HelloWorld(Resource):
    def get(self, name):
        if name in books:
            return books[name]
        else:
            return {"error": "Book not found"}, 404

    def post(self, name):
        # Retrieve data from the POST request body
        data = request.get_json()
        if data:
            # Update or create a book entry
            books[name] = data
            return {"message": f"Book '{name}' updated successfully"}, 201
        else:
            return {"error": "Invalid data in the request body"}, 400

api.add_resource(HelloWorld, "/helloworld/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)




