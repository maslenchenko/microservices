from flask import Flask, request, jsonify
import requests
import uuid
import random
import hazelcast

app = Flask(__name__)

client = hazelcast.HazelcastClient()

LOGGING_SERVICE_URLS = ['http://localhost:5001/log', 'http://localhost:5002/log', 'http://localhost:5003/log']
MESSAGES_SERVICE_URLS = ['http://localhost:5004/message', 'http://localhost:5005/message'] 

@app.route('/facade', methods=['POST'])
def handle_post():
    if not request.is_json:
        return jsonify({'error': 'request must be JSON'}), 400
    data = request.json
    message_id = uuid.uuid4().hex
    msg = data['msg']

    queue = client.get_queue('message_queue').blocking()
    
    try:
        queue.put({'msg': msg, 'uuid': message_id})
    except Exception as e:
        return jsonify({'error': 'Failed to enqueue message'}), 503
    
    LOGGING_SERVICE_URL = random.choice(LOGGING_SERVICE_URLS)
    try:
        response = requests.post(LOGGING_SERVICE_URL, json={'msg': msg, 'uuid': message_id})
        if response.status_code != 200:
            return jsonify({'error': 'logging service error'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Logging service unavailable'}), 503

    return jsonify({'uuid': message_id}), 200

@app.route('/facade', methods=['GET'])
def handle_get():
    
    all_logs = []
    
    LOGGING_SERVICE_URL = random.choice(LOGGING_SERVICE_URLS)
    try:
        log_response = requests.get(LOGGING_SERVICE_URL)
        if log_response.status_code != 200:
            return jsonify({'error': 'logging service error'}), 500
        log_data = log_response.json()
        all_logs.extend(list(log_data))
    except requests.exceptions.RequestException:
        return jsonify({'error': 'logging service unavailable'}), 503

    MESSAGES_SERVICE_URL = random.choice(MESSAGES_SERVICE_URLS)
    try:
        message_response = requests.get(MESSAGES_SERVICE_URL)
        if message_response.status_code != 200:
            return jsonify({'error': 'messages service error'}), 500
        message_data = message_response.json()
    except requests.exceptions.RequestException:
        return jsonify({'error': 'messages service unavailable'}), 503
    combined_response = {'logs': all_logs, 'messages': message_data}
    return jsonify({'response': combined_response}), 200

if __name__ == '__main__':
    app.run(port=5000)
