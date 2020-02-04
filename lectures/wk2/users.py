from flask import Flask
app = Flask(__name__)

@app.route('/')
def info():
    return 'Append "u/{username}" to the end of the url to go to <i>username</i>\'s page'

@app.route('/u/<username>')
def show_profile(username):
    return f'This is {username}\'s user profile'