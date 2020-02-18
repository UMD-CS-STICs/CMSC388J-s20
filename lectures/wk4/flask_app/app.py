from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo

from flask_app.forms import WelcomeForm

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/my_database"
app.config['SECRET_KEY'] = b'z\x8b\x7fs\xb2\xfa\xeb\x1a\xe6\xa8\xcd\x81\xf2Qq\xdb'
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = WelcomeForm()
    if request.method == 'POST':
        if form.validate():
            user = {
                'name': form.name.data,
                'location': form.location.data,
                'age': form.age.data,
            }

            mongo.db.users.insert_one(user)
        else:
            print('validation failed')
        
        return redirect(request.path)

    message = None
    user = mongo.db.users.find_one()
    if user is not None:
        message = f'Welcome {user["name"]}, age {user["age"]}, of {user["location"]}'
    
    return render_template('index.html', title='Front page', message=message, form=form)



