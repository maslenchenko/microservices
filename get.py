import requests

FACADE_SERVICE_URL = 'http://localhost:5000/facade'

get_response = requests.get(FACADE_SERVICE_URL)
print('GET responce from facade-service:', get_response.json())