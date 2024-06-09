from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    jsonRes = {
        "message": "Hello Flask"
    }

    return jsonify(jsonRes)