import requests

FACADE_SERVICE_URL = 'http://localhost:5000/facade'

for i in range(1, 11):
    post_response = requests.post(FACADE_SERVICE_URL, json={'msg': f'msg{i}'})
    print('POST responce from facade-service:', post_response.json())