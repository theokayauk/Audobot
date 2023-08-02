import os
import sys
import messagefinder
from flask import Flask, make_response, render_template
from flask import Response
from flask import request as flask_request


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    return "Hello, World"

@app.route('/slack', methods=['POST'])
def helloo():
    return "Hello, World"


    
if __name__ == '__main__':
  app.run(debug=True)
    