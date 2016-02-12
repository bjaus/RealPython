# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use decorators to link the function to a URL
@app.route('/')
@app.route('/hello')
# define the view using a function, which returns a string
def hello_world():
	return "Hello, World!"

# dynamic route
@app.route('/test/<search_query>')
def search(search_query):
	return search_query

# dynamic route with explicit status codes	
@app.route('/name/<name>')
def index(name):
	if name.lower() == 'brandon':
		return 'Hello, {}!'.format(name.capitalize()), 200
	else:
		return 'Not Found', 404

# start the development server using the run() method
if __name__ == "__main__":
	app.run(debug=True)