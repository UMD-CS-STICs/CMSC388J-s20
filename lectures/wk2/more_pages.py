
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'Hello! Calling from CMSC388J<br>I\'m learning Flask!'
