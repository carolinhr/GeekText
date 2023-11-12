import requests

BASE = "http://127.0.0.1:5000/"

# for i in range(len(data)):
#     response = requests.post(BASE + "shoppingcart/0", data[i])
#     print(response)

# input()
# response = requests.delete(BASE + "shoppingcart/0/1")
# print(response)
# input()
response = requests.delete(BASE + "shoppingcart/1/2")
print(response)