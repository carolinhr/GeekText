import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name" : "textbook0", "author" : "author0", "price" : 60.00},
        {"name" : "textbook1", "author" : "author1", "price" : 65.00},
        {"name" : "textbook2", "author" : "author2", "price" : 70.00}]

# for i in range(len(data)):
#     response = requests.post(BASE + "shoppingcart/0", data[i])
#     print(response)

# input()
# response = requests.delete(BASE + "shoppingcart/0/1")
# print(response)
# input()
response = requests.get(BASE + "shoppingcart/0/subtotal")
print(response.json())