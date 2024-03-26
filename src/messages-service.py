from flask import Flask, jsonify
from hazelcast import HazelcastClient
from threading import Thread, Lock

app = Flask(__name__)

client = HazelcastClient()
messages = []
messages_lock = Lock()

@app.route('/message', methods=['GET'])
def get_message():
    with messages_lock:
        return jsonify(list(messages))

def consume_messages():
    queue = client.get_queue('message_queue').blocking()
    
    while True:
        try:
            item = queue.take()
            message_id = item['uuid']
            msg = item['msg']
            with messages_lock:
                messages.append(msg) 
            print(f'Message consumed: {msg} with UUID: {message_id}')
        except Exception as e:
            print('Failed to consume message', str(e))

if __name__ == '__main__':
    consumer_thread = Thread(target=consume_messages)
    consumer_thread.start()
    app.run(port=5005)
