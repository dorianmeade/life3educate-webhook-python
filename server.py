from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1', methods=['GET'])
def getType(): 
    if 'type' in request.args:
        mytype = request.args['type']
    else: 
        mytype = "none"

    return jsonify(type=mytype)
app.run()