# P3: Movie Ratings Database

**Assigned**: Week 4, February 20th, 2020

**Due**: Week 6, March 4th, 2020, 11:59 PM

**Late Deadline**: Refer to syllabus for the policy.

## Description

You will be constructing the forms and database-accessing parts of a movie rating
website so that users can search for movies and leave reviews for the world to see.

**Important Change:** We realized that we need to validate the form using the
`form.validate_on_submit()` syntax if we want the error messages to show up. This method will simply
validate the form input on a `POST` request, and any errors that you throw, or that the built-in
valiadators throw, will be available for display. After using `form.validate_on_submit()`, we
may still use `redirect()` to direct users to the `GET` method of our route or to another route
entirely.

## Setup

The setup involves getting an API key, setting it to an environment variable on your system, 
and installing the necessary packages. 

You must use your API key by setting an environment variable. While it is possible to
paste it directly in the code, we strongly advise against doing that, as it is a security hazard.
We should not be able to see your API key in your submitted files, but we should be able to
run your code with our own API keys. 

You may set the environment variable for your API key each time you open a shell, but that's
also tedious to do, so we've included instructions here on how to set environment variables
permanently on your system (until you remove them, of course).

### Setup (OMDb):
1. Navigate to The Open Movie Database website -- http://www.omdbapi.com/
   ![alt text](images/omdb_home.png "The OMDb homepage")
2. Request an API key and navigate to the email you used to sign up with OMDb, and
   verify your API key.
   ![alt text](images/request_key.png "Request an API Key")
3. Using the API key you received in your email, set the environment variable
   `OMDB_API_KEY` on your system, so that the `MovieClient` script executes without error.

### Setting permanent environment variables (Unix)
1. If you're on macOS Catalina, then you have the `zsh` shell in your Terminal by default. If
   you're on a Linux distribution, then you mostly likely have `bash`, but the instructions
   still apply. **To determine which shell you're using,** use this command: `echo "$SHELL"`.
   (If you're using `fish`, you probably know how to set environment variables already)
2. Open the the `~/.bashrc` or `~/.zshrc` for modification using your favorite text editor (nano
   works perfectly fine for this, we're adding one line.)
3. Somewhere in the file, preferably at the end so you can easily find it, type
   `export OMDB_API_KEY={your_key_here}`, with your own key. 
   You don't need quotes around the API key. Restart your shell application if you haven't
   already, and your environment variable should be set. You can use the command
   `env | grep "OMDB_API_KEY"` in your shell to check if it is.
4. (Optional) After the project, you can remove the API key from your system by deleting
   the relevant snippet in `~/.bashrc` or `~/.zshrc`.

### Setting permanent environment variables (Powershell)
1. Search for "environment variables" in the Windows start menu  
   ![alt text](images/env_var_windows_search.png "Searching for Environment Variable Settings")  
2. Click on the "Environment Variables..." button  
   ![alt text](images/env_var_sys_props.PNG "System Properties Window")  
3. Click on the "New..." button under "User Variables for <username>"  
   ![alt text](images/env_var_window.PNG "Environment Variables Window")  
4. Enter the desired environment variable name (`OMDB_API_KEY`) under "Variable name"
   and your key under "Variable value"  
   ![alt text](images/env_var_set_new_var.PNG "Set New Variable")  

You must use your API key by setting environment variables. We can't enforce it, but please don't
paste the key into your code.

To create your virtual environment, be in the `p3/` directory and use
the correct command to create a virtual environment folder named `venv`. To activate it,
use the appropriate command for your system (if you're having trouble
figuring out how to activate your environment, contact us and include a 
screenshot of the `venv` directory structure).
Then, to install the necessary packages, run `pip install -r requirements.txt`.

This week we'll be using the `requests`, `Flask`, `Flask-WTF`, and `Flask-PyMongo` libraries.

## Project

This is the `p3/` directory structure
.
├── README.md
├── flask_app
│   ├── __init__.py
│   ├── app.py
│   ├── forms.py
│   ├── model.py
│   ├── static
│   │   └── custom.css
│   └── templates
│       ├── base.html
│       ├── header.html
│       ├── index.html
│       ├── movie_detail.html
│       └── query.html
├── images
│   ├── env_var_set_new_var.PNG
│   ├── env_var_sys_props.PNG
│   ├── env_var_window.PNG
│   ├── env_var_windows_search.png
│   ├── omdb_home.png
│   └── request_key.png
└── requirements.txt

**Only modify:** `app.py` and `forms.py`. 

There's a README, this document, containing your instructions to complete the project. The
`images/` folder consists of images used in the README, so it is not anything
you have to worry about while implementing your project. `requirements.txt` contains
all of the packages you should have installed (with `pip install -r requirements.txt`).

The `flask_app/` directory contains `app.py`, where all of your view functions and app setup
are located, `forms.py`, containing the two forms you will have to implement, `model.py`,
which provides two classes: `Movie` and `MovieClient`, which is how you'll interact with the
OMDb API, a `static/` folder consisting of custom CSS (don't worry about this), and
`templates/`, consisting of all templates you'll use for this project. 

First, we'll explain `model.py`:
- `model.py` consists of two classes. One is a `Movie` class, the other `MovieClient`
- The `MovieClient` class is instansiated with an API key (don't worry about this
  once you've set your environment variable), and it has two methods for you to use:
  - `search()` takes a `search_string` that the user entered into the search box
    on the index page, and it either returns a `dict` containing an error message
    or a `list` of `Movie` objects. 
  - `retrieve_movie_by_id()` takes an `imdb_id` and returns a `Movie` object with more data
    on that particular movie. Once again, this function returns a `dict` containing
    an error message or a single `Movie` object.
- The `Movie` class consists of up to 10 attributes. If a detailed movie request is made, then
  it contains all 10. Otherwise, if just being searched for using `MovieClient.search()`, it will
  have the basic 5 attributes (title, year, imdb_id, type, poster_url).


Here's what you need to do for this project, file by file:
1. `app.py`:
   - Set the database and secret keys, so that Mongo works and the CSRF tokens
      can be generated. 
   - In `query_results(query)`, you'll need to use the `MovieClient` class to search 
     movies matching `query`. If an error is encountered, (when a `dict` is returned),
     an error message should be displayed, and no query results. If the search is
     successful (list of `Movie`s returned), then display those Movies (the template
     is taken care of)
   - In `movie_detail(movie_id)`, use the `MovieClient` class to get a detailed
     view of the movie identified by `movie_id`. If it has a retrieval error (`dict` returned), 
     show the error message. If no error, then create the MovieReviewForm. Then 
     if `validate_on_submit()` is true, store the movie review with 
     **4 paramters: `imdb_id`, `commenter`, `content`, and `date`**. You can store
     the data into any collection, but make sure you're keeping track of collections.
     That said, we require you **use one collection for all reviews.**
     After successful storing, redirect so the user can see their published review. 
   - Additionally in `movie_detail(movie_id)`, all of the reviews that users have submitted
     for that movie must be displayed. The template takes care of displaying, you have to
     provide the data.
   - **Note:** There is a `current_time()` function at the bottom of `app.py` that returns
     the current date and time as a neatly-formatted string.
   - **Second note:** To determine what parameters to pass in to templates, peruse the templates.
2. `forms.py`:
   - Create the two forms `SearchForm` and `MovieReviewForm`.
   - `SearchForm` has a text-box for entering a query, and a submit button. Check out
     the `index()` view function and the `index.html` template
     to see what the form elements should be named.
     The query should be at least 1 character long, but no more than 30.
   - `MovieReviewForm` has a text-box for a commenter to enter their name or an alias, and
     a larger text area for a commenter to type out the full content of their post, along
     with a button for submission. A name should be at least 1 character long, no more than 50, and the content of a comment
     should be at least 1 character, but no more than 500. 
     The names for these fields can be determined by looking at the `movie_detail.html` template.

**Hint for MovieReviewForm:** You should use a field that allows multi-line input.

## Testing

Please make sure you haven't modified the template files.

When your current directory is `flask_app/`, you can simply run the command `flask run`
in your terminal or command line to see your website.

Make sure the index page shows up, and that you can enter queries for movies in the form.
If any errors occur while querying, the error message should be shown on the query page.
If no errors occurred, we should see a list of movie posters and titles. For exmaple, searching
`guardians` yields 113 results. Then clicking on one of these titles should take us to
the detail page. Here we see lots of extra information on the movie in a card at the top,
and we should see all the reviews users left below that, and then the form for submitting
reviews below that. If the movie detail retrieval fails, the error message for the failure should 
be displayed, without any of the reviews or the form being displayed.

The navbar header should take you back to the main page, where you can search for more movies.

**We will be** releasing a demo video within the next couple of days.

## Submissions

Assure that you've tried out all the different things that could go wrong and that they
are behaving appropriately (and the things that are supposed to work, still do).

**The directory, along with its contents, should be zipped, not the contents of the directory.**
In other words, when we unzip your file, we should see the `flask_app/` directory. If you
have any questions on how to submit, please contact us.

If you don't submit according to the instructions above, you may lose **up to 25%** of your
score on this project.

After zipping, submit the zip file to the appropriate ELMS page. No test results will be shown.

We'll release a demo video and grading guidelines in a few days.
