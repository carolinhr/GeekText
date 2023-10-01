import requests

BASE = "http://127.0.0.1:5000/"

# Specify the name parameter in the URL
book_name = "book1"

# JSON data to send in the request body
data = {
    "Review": "Excellent",
    "Rating": 10
}

response = requests.post(BASE + f"helloworld/{book_name}", json=data)

if response.status_code == 201:
    print("Book Information Updated Successfully.")
else:
    print("Error:", response.json())

