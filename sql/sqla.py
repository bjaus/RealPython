# Create a SQLite3 database and table

# import the sqlite3
import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect('cars.db')

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute("""CREATE TABLE inventory
	(Make TEXT, Model TEXT, Quantity INT)""")

# Close the database connection
conn.close()