# project/db_create.py
# db_create.py: sets up and creates the database

from views import db 
from models import Task
from datetime import date 


# create the database and the db table
db.create_all()

# insert database
db.session.add(Task("Finish this tutorial", date(2016, 2, 20), 10, 1))
db.session.add(Task("Finish Real Python", date(2016, 4, 20), 10, 1))

# commit the changes
db.session.commit()