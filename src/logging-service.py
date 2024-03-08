from flask import Flask, request, jsonify
import uuid
import hazelcast

app = Flask(__name__)
client = hazelcast.HazelcastClient()
messages_map = client.get_map('messages').blocking()

@app.route('/log', methods=['POST'])
def log_message():
    data = request.json
    message_id = uuid.uuid4().hex
    msg = data['msg']
    messages_map.put(message_id, msg)
    print(f'new message received, UUID: {message_id}, message: {msg}')
    return jsonify({'uuid': message_id}), 200

@app.route('/log', methods=['GET'])
def get_messages():
    all_messages = list(messages_map.values())
    return jsonify(all_messages), 200

if __name__ == '__main__':
    app.run(port=5002)
