from flask import Flask, jsonify
import os
import random
from backend.blockchain.blockchain import Blockchain
from backend.pubsub import PubSub
app = Flask(__name__)

blockchain = Blockchain()
pubsub = PubSub()


@app.route('/')

def default():
    return f'<h1>Welcome to the blockchain</h1>'

@app.route('/blockchain')

def route_blockchain():
    return jsonify(blockchain.chain[-1].to_json())

PORT = 5000

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001,6000)


app.run(port=PORT)


