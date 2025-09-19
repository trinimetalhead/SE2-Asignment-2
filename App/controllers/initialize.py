from .user import *
from .internship import *
from .shortlist import *
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_student(username='alice', password='alicepass', first_name='Alice', last_name='Johnson', major='Computer Science')
    create_staff('alice_in_wonderland', 'alicepass', 'Alice', 'Smith', position='Administrator')
    create_employer('emily', 'emilypass', 'Emily', 'Davis', company='Tech Corp')

    employer = get_user_by_username('emily')
    if employer and employer.role == 'employer':
        internship1 = InternshipPosition(title='Software Engineering Intern', description='Work on developing software solutions.', requirements='Knowledge of Python and Java.', employer_id=employer.id)
        internship2 = InternshipPosition(title='Data Science Intern', description='Assist in data analysis and modeling.', requirements='Familiarity with data analysis tools.', employer_id=employer.id)

    print ("Database initialized with sample data.")