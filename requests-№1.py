import json
import requests

# #Тип запроса GET
status='available'
headers = {'accept': 'application/json', "Content-Type" : "application/json"}
res1 = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = headers)
print(res1.json())
print(res1.status_code)

#Тип запроса POST
status='available'
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data = json.dumps(data)
headers = {'accept':'application/json', "Content-Type":"application/json"}
res2 = requests.post( f"https://petstore.swagger.io/v2/pet", headers=headers, data=data)

print(res2.json())
print(res2.status_code)


# Тип запроса PUT

headers = {'accept': 'application/json', "Content-Type" : "application/json"}
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggieGYGY",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
data = json.dumps(data)
res3 = requests.put( f"https://petstore.swagger.io/v2/pet", headers=headers, data=data)

print(res3.json())
print(res3.status_code)


# Тип запроса DELETE

headers = {'accept': 'application/json', 'api_key':'special-key'}

res4 = requests.delete( f"https://petstore.swagger.io/v2/pet/9223372036854290925", headers=headers)
# В конце адреса нужно подставить ID существующего в базе животного для удаления
print(res4.status_code)






