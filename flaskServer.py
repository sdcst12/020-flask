#!python3
from flask import Flask, request
from flask_cors import CORS
import time, json

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    return "Hello World"

@app.route("/html")
def html():
    return "<h1>Hello World</h1>"

@app.route("/json")
def jsondata():
    output = {
        "greeting" : "Hello World",
        "success" : 100,
        "timestamp" : time.time()
    }
    x = request.args
    x = dict(x)
    print(f"data is: {x}")
    return json.dumps(output)
app.run()
