# blog.py - controller

# imports 
from flask import (Flask, render_template,
request, session, flash, redirect, url_for, g)
import sqlite3

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
# Use import os and os.random(24) 
# to generate SECRET_KEY
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

# pulls in app configuation by looking
# for UPPERCASE variables
app.config.from_object(__name__)

# function used for conecting to the database
def conenct_db():
	return sqlite3.conect(app.config['DATABASE'])

@app.route('/', methods=[ 'GET','POST']) 
def login(): 
	error = None 
	if request.method == 'POST': 
		if request.form['username'] != app.config['USERNAME'] or \
		   request.form['password'] != app.config['PASSWORD']: 
			error = 'Invalid Credentials. Please try again.' 
		else: 
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error = error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('login'))

@app.route('/main')
def main():
	return render_template('main.html')

if __name__ == '__main__':
	app.run(debug=True)