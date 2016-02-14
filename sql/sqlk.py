# JOIN data from multiple tables

import sqlite3

with sqlite3.connect('new.db') as connection:
	c = connection.cursor()

	# retrieve data
	c.execute("""
		SELECT DISTINCT p.city, p.population, r.region
		FROM population p, regions r
		WHERE p.city = r.city
		ORDER BY p.population DESC""")

	rows = c.fetchall()

	for r in rows:
		print("""
City: {}
Population: {}
Region: {}
""".format(r[0],r[1],r[2]))