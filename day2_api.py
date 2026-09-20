import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

print(data)

for user in data:
    print(user["name"])

for user in data:
    print("Name:", user["name"])
    print("City:", user["address"]["city"])
    print()
