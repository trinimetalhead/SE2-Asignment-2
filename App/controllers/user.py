from App.models import User, Staff, Student, Employer
from App.database import db
 
# CREATE

def create_student(username, password, first_name, last_name, major='undeclared'):
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    
    student = Student(username, password, first_name, last_name, major)
    db.session.add(student)
    db.session.commit()

def create_staff(username, password, first_name, last_name, position='Staff Member'):
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    
    staff = Staff(username, password, first_name, last_name, position)
    db.session.add(staff)
    db.session.commit()

def create_employer(username, password, first_name, last_name, company='Unknown Company'):
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    
    employer = Employer(username, password, first_name, last_name, company)
    db.session.add(employer)
    db.session.commit()



def get_user_by_username(username):
    result = db.session.execute(db.select(User).filter_by(username=username))
    return result.scalar_one_or_none()

def get_user(id):
    return db.session.get(User, id)

def get_all_users():
    return db.session.scalars(db.select(User)).all()

def get_all_users_json():
    users = get_all_users()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        # user is already in the session; no need to re-add
        db.session.commit()
        return True
    return None

def get_user_by_role(role):
    return User.query.filter_by(role=role).all()

def get_all_students():
    return get_user_by_role('student')

def get_all_employers():
    return get_user_by_role('employer')

def get_all_staff():
    return get_user_by_role('staff')

