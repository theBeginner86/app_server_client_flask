import json
from flask import Flask, Response

app = Flask(__name__)


@app.route("/health", methods=['GET'])
def health():
	message = json.dumps({
		'result': "Hello Client!!"
	})
	status_code = 200
	header = {
		'Content-Type': 'application/json'
	}
	return Response(message, status_code, header)
