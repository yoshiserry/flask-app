#import libraries
from flask import Flask, render_template, request, session, redirect, url_for
import os
import sqlite3
import pandas as pd
from dbhelper import *
from flask_sqlalchemy import SQLAlchemy
import os

#create app
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
# create the sqlalchemy object
db = SQLAlchemy(app)

# import db schema
from models import *

#create url for index or homepage aka route.
@app.route("/")
def index():
    blog_posts = db.session.query(BlogPost).all()
    return render_template('homepage.html', blog_posts=blog_posts)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

#run the app on localhost port 5000
#if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
#    port = int(os.environ.get('PORT', 8000))
#    app.run(debug=False, host='0.0.0.0', port=port)

# start the server with the 'run()' method
if __name__ == '__main__':
app.run()
