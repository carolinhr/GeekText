import requests

BASE = "http://127.0.0.1:5000/returnjson"

response = requests.get(BASE + "returnjson")
print(response.text)