posts = [
    {
        'user': 'Elon Musk',
        'text': 'The sun is a theronuclear explosion fyi',
        'location': 'California',
        'likes': f'{99_700:,d}',
    },
    {
        'user': 'John Smith',
        'text': 'Excited for school!!!!',
        'location': 'College Park',
        'likes': f'{5:,d}'
    }
]

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

@app.route('/feed')
def feed():
    return render_template('posts.html', posts=posts, title='The Feed')

@app.route('/u/<username>')
def profile(username):
    return f'This is {username}\'s user profile'


