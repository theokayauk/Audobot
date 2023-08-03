import os
import sys
import messagefinder
from flask import Flask, make_response, render_template
from flask import Response
from flask import request as flask_request
import messagefinder

import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

bot_token = 'xoxb-145080091058-5433144011491-7SYgz3ZgdARIykMx10lLxvl0'


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello, World"

@app.route('/saysomething', methods=['POST'])
def helloo():
    client = WebClient(token= bot_token)

    payload = flask_request.get_json()

    mess = client.chat_postMessage(channel='C05KW8HL6SZ', text='hey buddy')

    
if __name__ == '__main__':
  app.run()


    