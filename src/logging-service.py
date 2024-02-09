from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
messages = {}

@app.route('/log', methods=['POST'])
def log_message():
    data = request.json
    message_id = uuid.uuid4().hex
    messages[message_id] = data['msg']
    print(f'new message received, UUID: {message_id}, message: {data["msg"]}')
    return jsonify({'uuid': message_id}), 200

@app.route('/log', methods=['GET'])
def get_messages():
    all_messages = list(messages.values())
    return jsonify(all_messages), 200

if __name__ == '__main__':
    app.run(port=5001)
