from flask import Flask, request, jsonify
import uuid
import hazelcast

app = Flask(__name__)
client = hazelcast.HazelcastClient()
logs_map = client.get_map('logs').blocking()

@app.route('/log', methods=['POST'])
def log_message():
    data = request.json
    message_id = uuid.uuid4().hex
    msg = data['msg']
    logs_map.put(message_id, msg)
    print(f'new message received, UUID: {message_id}, message: {msg}')
    return jsonify({'uuid': message_id}), 200

@app.route('/log', methods=['GET'])
def get_messages():
    all_messages = list(logs_map.values())
    return jsonify(all_messages), 200

if __name__ == '__main__':
    app.run(port=5001)
