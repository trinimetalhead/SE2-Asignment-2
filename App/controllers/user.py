from App.models import User
from App.database import db

def create_user(username, password, first_name, last_name, role, **kwargs):
    from App.models import User, Student, Staff, Employer
    #check if username already exists
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    

    
    newuser = User(username=username, password=password, first_name=first_name, last_name=last_name, role=role)
    db.session.add(newuser)
    db.session.commit()

    #create profile based on role

    if role == 'student':
        profile = Student(user_id = newuser.id, major= kwargs.get('major','undeclared'))
    elif role == 'staff':
        profile = Staff(user_id = newuser.id, position= kwargs.get('position','Staff Member'))
    elif role == 'employer':
        profile = Employer(user_id = newuser.id, company= kwargs.get('company','Unknown Company'))

    db.session.add(profile)
    db.session.commit()

    return newuser

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

