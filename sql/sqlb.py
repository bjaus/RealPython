# Create a SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect('new.db')

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
cursor.execute("INSERT INTO population \
	VALUES('New York City', 'NY', 8200000)")
cursor.execute("INSERT INTO population \
	VALUES('San Francisco', 'CA', 800000)")

# commit the changes
conn.commit()

# Close the database connection
conn.close()

# Similar script that doesn't require commit() to be called
"""
import sqlite3
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO population \
	VALUES 'New York City', 'NY', 8200000")
	c.execute("INSERT INTO population \
	VALUES('San Francisco', 'CA', 8000000)")
"""
