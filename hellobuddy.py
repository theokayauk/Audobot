import os
import sys
import messagefinder
from flask import Flask, make_response, render_template
from flask import Response
from flask import request as flask_request


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return Response("Hello, World!"), 200

@app.route('/verify', methods=['POST'])
def inbound():
    """
    Inbound POST from Slack to test token
    """
    # When Slack sends a POST to your app, it will send a JSON payload:
    payload = flask_request.get_json()

    # This response will only be used for the initial URL validation:
    if payload:
        return Response(payload['challenge']), 200
    
    