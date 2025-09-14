from .user import *
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass', 'Bob', 'Smith', 'student', major='Computer Science')
    create_user('alice', 'alicepass', 'Alice', 'Johnson', 'staff', position='Administrator')
    create_user('emily', 'emilypass', 'Emily', 'Davis', 'employer', company='Tech Corp')

    print ("Database initialized with sample data.")