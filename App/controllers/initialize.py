from .user import *
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass', 'Bob', 'Smith', 'student')
    
