# Creates the database based on the models we've defined in models.py


from config import SQLALCHEMY_DATABASE_URI
from app import db, models
db.create_all()

