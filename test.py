import requests

FACADE_SERVICE_URL = 'http://localhost:5000/facade'

post_response = requests.post(FACADE_SERVICE_URL, json={'msg': 'test message 1'})
print('POST responce from facade-service:', post_response.json())

get_response = requests.get(FACADE_SERVICE_URL)
print('GET responce from facade-service:', get_response.json())

post_response = requests.post(FACADE_SERVICE_URL, json={'msg': 'test message 2'})
print('POST responce from facade-service:', post_response.json())

get_response = requests.get(FACADE_SERVICE_URL)
print('GET responce from facade-service:', get_response.json())