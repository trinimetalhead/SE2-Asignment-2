from .user import *
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_student(username='alice', password='alicepass', first_name='Alice', last_name='Johnson', major='Computer Science')
    create_staff('alice_in_wonderland', 'alicepass', 'Alice', 'Smith', position='Administrator')
    create_employer('emily', 'emilypass', 'Emily', 'Davis', company='Tech Corp')

    print ("Database initialized with sample data.")