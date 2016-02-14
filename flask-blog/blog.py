# blog.py - controller

# imports 
from flask import (Flask, render_template,
request, session, flash, redirect, url_for, g)
import sqlite3

# configuration
DATABASE = 'blog.db'

app = Flask(__name__)

# pulls in app configuation by looking
# for UPPERCASE variables
app.config.from_object(__name__)

# function used for conecting to the database
def conenct_db():
	return sqlite3.conect(app.config['DATABASE'])

if __name__ == '__main__':
	app.run(debug=True)