# 3rd-party packages
from flask import render_template, request, redirect, url_for, flash, Response
from flask_mongoengine import MongoEngine
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename

# stdlib
from datetime import datetime

# local
from . import app, bcrypt, client
from .forms import (SearchForm, MovieReviewForm, RegistrationForm, LoginForm,
                             UpdateUsernameForm, UpdateProfilePicForm)
from .models import User, Review, load_user
from .utils import current_time

""" ************ View functions ************ """
@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    if form.validate_on_submit():
        return redirect(url_for('query_results', query=form.search_query.data))

    return render_template('index.html', form=form)

@app.route('/search-results/<query>', methods=['GET'])
def query_results(query):
    results = client.search(query)

    if type(results) == dict:
        return render_template('query.html', error_msg=results['Error'])
    
    return render_template('query.html', results=results)

@app.route('/movies/<movie_id>', methods=['GET', 'POST'])
def movie_detail(movie_id):
    result = client.retrieve_movie_by_id(movie_id)

    if type(result) == dict:
        return render_template('movie_detail.html', error_msg=result['Error'])

    form = MovieReviewForm()
    if form.validate_on_submit():
        review = Review(
            commenter=load_user(current_user.username), 
            content=form.text.data, 
            date=current_time(),
            imdb_id=movie_id,
            movie_title=result.title
        )

        review.save()

        return redirect(request.path)

    reviews = Review.objects(imdb_id=movie_id)

    print(current_user.is_authenticated)

    return render_template('movie_detail.html', form=form, movie=result, reviews=reviews)

@app.route('/user/<username>')
def user_detail(username):
    return 'user_detail'

"""
EXTRA CREDIT: Refer to the README
"""
@app.route('/images/<username>')
def images(username):
    pass


""" ************ User Management views ************ """
@app.route('/register', methods=['GET', 'POST'])
def register():
    return 'register'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'login'

@app.route('/logout')
@login_required
def logout():
    return 'logout'

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    return 'account'
