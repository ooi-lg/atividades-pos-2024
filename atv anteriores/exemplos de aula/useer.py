import requests
user_id = input("digite o id")
response = requests.get("http://jsonplaceholder.typicode.com/users/{user_id}")

print(response.status_code)
user = response.json()
print(f"{user['name']} - {user['email']}")