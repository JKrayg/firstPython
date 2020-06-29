# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

#Sample JSON
userJSON = '{"firstname": "John", "lastname": "Doe", "age": "21"}'

#Parse to dict
user = json.loads(userJSON)
print(user['firstname'])
print(user)

car = {"make": "ford", "model": "mustang", "year": "1970"}

carJSON = json.dumps(car)

print(carJSON)