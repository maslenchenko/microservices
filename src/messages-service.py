from flask import Flask, jsonify
from hazelcast import HazelcastClient

app = Flask(__name__)

client = HazelcastClient()
messages_map = client.get_map("messages").blocking()

@app.route('/message', methods=['GET'])
def get_message():
    messages_dict = messages_map.entry_set()
    messages = [message[1] for message in messages_dict]
    return jsonify(messages)

if __name__ == '__main__':
    app.run(port=5004)
