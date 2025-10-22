from App.models import User, Staff, Student, Employer
from App.database import db
 
# CREATE

def create_student(username, password, first_name, last_name, major='undeclared'):
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    
    student = Student(username, password, first_name, last_name, major)
    db.session.add(student)
    db.session.commit()
    return student

def create_staff(username, password, first_name, last_name, position='Staff Member'):
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    
    staff = Staff(username, password, first_name, last_name, position)
    db.session.add(staff)
    db.session.commit()
    return staff

def create_employer(username, password, first_name, last_name, company='Unknown Company'):
    if User.query.filter_by(username=username).first():
        raise ValueError("Username already exists")
    
    employer = Employer(username, password, first_name, last_name, company)
    db.session.add(employer)
    db.session.commit()
    return employer


#READ
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


def get_user_by_role(role):
    return User.query.filter_by(role=role).all()

def get_all_students():
    return get_user_by_role('student')
            
def get_all_employers():
    return get_user_by_role('employer')

def get_all_staff():
    return get_user_by_role('staff')

def check_user_role (id, requiredRole):
    user = get_user(id)
    if user and user.role == requiredRole:
        return True
    return False

def get_user_role(id):
    user = get_user(id)
    return user.role if user else print(f"Error")

def is_student(id):
    return check_user_role(id, 'student') 

def is_staff(id):
    return check_user_role(id, 'staff')

def is_employer(id):
    return check_user_role(id,'employer')

#UPDATE 
def update_username(id,newUsername):
    user = get_user(id)
    if user:
        user.update_username(newUsername)
        # user is already in the session; no need to re-add
        db.session.commit()
        return True
    else:
        return print(f"User with ID {id} not found!")
    
def update_firstname(id,newFirstName):
    user = get_user(id)
    if user:
        # Fix: Change update_first_name to update_firstname
        user.update_firstname(newFirstName)
        db.session.commit()
        return True
    else:
        return print(f"No user with ID {id} found!")
    
def update_lastname(id,newLastName):
    user = get_user(id)
    if user:
        user.update_lastname(newLastName)
        db.session.commit()
        return True
    else:
        return print(f"No user with ID {id} found!")
    
def update_password(id,newPassword):
    user=get_user(id)
    if user:
        user.update_password(newPassword)
        db.session.commit()
        return True
    else:
        return print(f"No user with ID {id} found!")

# Combined update function
def update_user(id, username=None, password=None, first_name=None, last_name=None):
    user = get_user(id)
    if not user:
        return False
    
    if username:
        user.update_username(username)
    if password:
        user.update_password(password)
    if first_name:
        user.update_first_name(first_name)
    if last_name:
        user.update_lastname(last_name)
    
    db.session.commit()
    return True

#DELETE
def delete_user(id):
    user = get_user(id)
    if user:
        user.delete()
        db.session.commit()
        return True
    return False