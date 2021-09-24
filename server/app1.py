from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/health', method=['GET'])
def health():
    message = jsonify({'result': 'Hello Client!!'})
    return message
