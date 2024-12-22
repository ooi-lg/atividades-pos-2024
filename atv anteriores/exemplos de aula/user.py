import requests
response = requests.get("http://jsonplaceholder.typicode.com/users")

print(response.status_code)
for user in response.json():
    print(f"{user['name']} - {user['email']}")