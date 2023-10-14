import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name" : "textbook1", "author" : "author1", "price" : 60.00},
        {"name" : "textbook2", "author" : "author2", "price" : 65.00},
        {"name" : "textbook3", "author" : "author3", "price" : 70.00}]

for i in range(len(data)):
    response = requests.put(BASE + "shoppingcart/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "shoppingcart/0")
print(response)
input()
response = requests.get(BASE + "shoppingcart/0")
print(response.json())