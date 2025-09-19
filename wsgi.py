import click, pytest, sys
from flask.cli import with_appcontext, AppGroup
from App.database import db, get_migrate
from App.models import User, internship_position, Shortlist 
from App.main import create_app
from App.controllers import *


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)


# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 
# Then define the command and any parameters and annotate it with the group (@)

#CREATE
@user_cli.command("create-student", help="Creates a student user")
@click.argument("username", default="alice")
@click.argument("password", default="alicepass")
@click.argument("first_name", default="Alice")
@click.argument("last_name", default="Johnson")
@click.argument("major", default="Computer Science")
def create_student_command(username, password, first_name, last_name, major):
    try:
        create_student(username, password, first_name, last_name, major)
        print(f'Student {username} created!')
    except ValueError as e:
        print(F"error: {e}")

@user_cli.command("create-staff", help="Creates a staff user")
@click.argument("username", default="john")
@click.argument("password", default="johnpass")
@click.argument("first_name", default="John")
@click.argument("last_name", default="Doe")
@click.argument("position", default="Lecturer")
def create_staff_command(username,password,first_name,last_name,position):
    try:
        create_staff(username,password,first_name,last_name,position)
        print(f'Staff {username} created!')
    except ValueError as e:
        print(F"error: {e}")

@user_cli.command("create-employer", help="Creates an employer user")
@click.argument("username", default="emily")
@click.argument("password", default="emilypass")
@click.argument("first_name", default="Emily")
@click.argument("last_name", default="Davis")
@click.argument("company", default="Tech Corp")
def create_employer_command(username,password,first_name,last_name,company):
    try:
        create_employer(username,password,first_name,last_name,company)
        print(f'Employer {username} created!')
    except ValueError as e:
        print(F"error: {e}")

#READ

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

@user_cli.command("list-staff", help="Lists all staff users in the database")
def list_staff_command():
    staff = [user for user in get_all_users() if user.role == 'staff']
    if not staff:
        print("No staff users found.")
        return
    for user in staff:
        print(f"ID: {user.id}, Username: {user.username}, Name: {user.first_name} {user.last_name}, Position: {user.position}")

@user_cli.command("list-employers", help="Lists all employer users in the database")
def list_employers_command():
    employers = [user for user in get_all_users() if user.role == 'employer']
    if not employers:
        print("No employer users found.")
        return
    for user in employers:
        print(f"ID: {user.id}, Username: {user.username}, Name: {user.first_name} {user.last_name}, Company: {user.company}")

@user_cli.command("list-students", help="Lists all student users in the database")
def list_students_command():
    students = [user for user in get_all_users() if user.role == 'student']
    if not students:
        print("No student users found.")
        return
    for user in students:
        print(f"ID: {user.id}, Username: {user.username}, Name: {user.first_name} {user.last_name}, Major: {user.major}")

#UPDATE

@user_cli.command("update-username", help="Updates a user's username")
@click.argument("user_id")
@click.argument("new_username")
def update_username_command(user_id, new_username):
    user = update_user(user_id, username=new_username)
    if user:
        print(f"User {user_id} username updated to {new_username}")
    else:
        print(f"User {user_id} not found.")

@user_cli.command("update-first-name", help="Updates a user's first name")
@click.argument("user_id") 
@click.argument("new_first_name")
def update_first_name_command(user_id, new_first_name):
    user = update_user(user_id, first_name=new_first_name)
    if user:
        print(f"User {user_id} first name updated to {new_first_name}")
    else:
        print(f"User {user_id} not found.")

@user_cli.command("update-last-name", help="Updates a user's last name")
@click.argument("user_id")
@click.argument("new_last_name")
def update_last_name_command(user_id, new_last_name):
    user = update_user(user_id, last_name=new_last_name)
    if user:
        print(f"User {user_id} last name updated to {new_last_name}")
    else:
        print(f"User {user_id} not found.")

@user_cli.command("update-password", help="Updates a user's password")
@click.argument("user_id")
@click.argument("new_password")
def update_password_command(user_id, new_password):
    user = update_user(user_id, password=new_password)
    if user:
        print(f"User {user_id} password updated.")
    else:
        print(f"User {user_id} not found.")



#DELETE

@user_cli.command("delete", help="Deletes a user from the database")
@click.argument("user_id")
def delete_user_command(user_id):
    result = delete_user(user_id)
    if result:
        print(f"User {user_id} deleted.")
    else:
        print(f"User {user_id} not found.")


'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

app.cli.add_command(test)


'''
Employer Commands
'''

employer_cli = AppGroup('employer', help='Employer commands') 

#CREATE
@employer_cli.command("create-position", help="Creates an internship position")
@click.argument("employer_id")
@click.argument("title", default="Intern")
@click.argument("description", default="Internship position description")
@click.argument("requirements", default="3.0 GPA or Above")
def create_position(employer_id, title, description, requirements):
    positions = create_internship_position(employer_id,title,description,requirements)
    print(f"position {positions.title} created with id {positions.id}")

#READ
@employer_cli.command("list-positions", help="Lists all internship positions for an employer")
@click.argument("employer_id")
def list_positions(employer_id):
    positions = get_internships_by_employer(employer_id)
    if not positions:
        print("No positions found for this employer.")
        return
    for position in positions:
        print(f"ID: {position.id}, Title: {position.title}, Description: {position.description}, Requirements: {position.requirements}")

@employer_cli.command("list-positions-employer", help="Lists all internship positions by employer")
@click.argument("employer_id")
def list_positions_by_employer(employer_id):
    positions = get_positions_by_employer(employer_id)
    if not positions:
        print("No positions found for this employer.")
        return
    for position in positions:
        print(f"ID: {position.id}, Title: {position.title}, Description: {position.description}, Requirements: {position.requirements}")

@employer_cli.command("view-shortlists", help="View all shortlists for a position")
@click.argument("position_id")
def view_shortlists_command(position_id):
    shortlists = get_shortlists_position(position_id)
    if not shortlists:
        print(f"No students shortlisted for position {position_id}.")
        return
    position = get_position_id(position_id)
    print(f"Shortlists for {position_id} {position.title}:")
    for shortlist in shortlists:
        student = get_user(shortlist.student_id)
        print(f"Shortlist ID: {shortlist.id}, Student: {shortlist.student_id} {student.first_name}_{student.last_name}, Status: {shortlist.status}, Date Added: {shortlist.date_added}")

#UPDATE

#update position not working
@employer_cli.command("update-position", help="Updates an internship position")
@click.argument("position_id")
@click.argument("field")
@click.argument("value")
def update_position(position_id, field, value):
    result = update_position(position_id, **{field: value})
    if result:
        print(f"Position {position_id} updated: {result}")
    else: 
        print(f"Position {position_id} not found.")

@employer_cli.command("update-posititon-title", help="Updates an internship position title")
@click.argument("position_id")
@click.argument("title")
def update_position_title(position_id, title):
    result = update_position_title(position_id, title)
    if result:
        print(f"Position {position_id} updated: {result}")
    else: 
        print(f"Position {position_id} not found.")

@employer_cli.command("update-position-description", help="Updates an internship position description")
@click.argument("position_id") 
@click.argument("description")
def update_position_description(position_id, description):
    result = update_position_description(position_id, description)
    if result:
        print(f"Position {position_id} updated: {result}")
    else: 
        print(f"Position {position_id} not found.")

@employer_cli.command("update-position-requirements", help="Updates an internship position requirements")
@click.argument("position_id") 
@click.argument("requirements")
def update_position_requirements(position_id, requirements):
    result = update_position_requirements(position_id, requirements)
    if result:
        print(f"Position {position_id} updated: {result}")
    else: 
        print(f"Position {position_id} not found.")

@employer_cli.command("accept", help="Accept a student for a position")
@click.argument("position_id")
@click.argument("student_id")
def accept_student_command(position_id, student_id):
    shortlists = get_shortlists_position(position_id)
    if not shortlists:
        return print(f"No students shortlisted for position {position_id}.")
    
    for shortlist in shortlists:
        if shortlist.student_id == int(student_id):
            shortlist.accept()
            print(f"Student {student_id} accepted for position {position_id}.")
            return
    return print(f"Student {student_id} not found in shortlist for position {position_id}.")



#DELETE

@employer_cli.command("delete-position",help="Deletes an Internship Position")
@click.argument("position_id")
def delete_position_command(position_id):
    delete_position(position_id)
    print(f"Position {position_id} deleted.")


app.cli.add_command(employer_cli) # add the group to the cli


'''
Staff Commands
'''

staff_cli = AppGroup('staff', help='staff commands') 

#CREATE
#create staff command under USER cli group

@staff_cli.command("add", help="Add a student to a position shortlist")
@click.argument("staff_id")
@click.argument("student_id")
@click.argument("position_id")
def add_to_shortlist_command(staff_id, student_id, position_id):
    try:
        shortlist = add_to_shortlist(staff_id, student_id, position_id)
        print(f"Student {student_id} added to shortlist for position {position_id} by staff {staff_id}. Shortlist ID: {shortlist.id}")
    except ValueError as e:
        print(f"Error: {e}")

#READ
@staff_cli.command("view-positions", help="View all internship positions")
def view_positions_command():
    positions = internship_position.InternshipPosition.query.all()
    if not positions:
        print("No internship positions found.")
        return
    for position in positions:
        employer = get_user(position.employer_id)
        print(f"ID: {position.id}, Title: {position.title}, Description: {position.description}, Requirements: {position.requirements}, Employer: {employer.id} {employer.first_name} {employer.last_name}")

@staff_cli.command("list-shortlists", help="Lists all shortlists in the database")
def list_shortlists_command():
    shortlists = get_all_shortlists()
    if not shortlists:
        print("No shortlists found.")
        return
    for shortlist in shortlists:
        print(f"Shortlist ID: {shortlist.id}, Position ID: {shortlist.position_id}, Student ID: {shortlist.student_id}, Status: {shortlist.status}, Date Added: {shortlist.date_added}")

@staff_cli.command("shortlisted-students", help="Get all shortlisted students for a position")
@click.argument("position_id")
def get_shortlisted_students_command(position_id):
    shortlists = get_shortlists_position(position_id)
    if not shortlists:
        print(f"No students shortlisted for position {position_id}.")
        return
    for shortlist in shortlists:
        print(f"Shortlist ID: {shortlist.id}, Student ID: {shortlist.student_id}, Status: {shortlist.status}, Date Added: {shortlist.date_added}")
    
@staff_cli.command("list-shortlists", help="Lists all shortlists in the database")
def list_shortlists_command():
    shortlists = get_all_shortlists()
    if not shortlists:
        print("No shortlists found.")
        return
    for shortlist in shortlists:
        position = get_position_id(shortlist.position_id)
        student = get_user(shortlist.student_id)
        staff = get_user(shortlist.staff_id) 
        print(f"Shortlist ID: {shortlist.id}, Position: {position.title}, Student: {shortlist.student_id}  {student.first_name}_{student.last_name}, Status: {shortlist.status}, Shortlisted by Staff: {shortlist.staff_id} {staff.first_name}_{staff.last_name} on {shortlist.date_added}")

#DELETE
@staff_cli.command("delete-shortlist", help="Deletes a shortlist entry")
@click.argument("shortlist_id")
def delete_shortlist_command(shortlist_id):
    try:
        delete_shortlist(shortlist_id)
        print(f"Shortlist {shortlist_id} deleted.")
    except ValueError as e:
        print(f"Error: {e}")

app.cli.add_command(staff_cli) # add the group to the cli


'''
Student Commands
'''

student_cli = AppGroup('student', help='student commands')

@student_cli.command("view-shortlists", help="View all shortlists for a student")
@click.argument("student_id")
def view_shortlists_command(student_id):
    shortlists = get_shortlists_student(student_id)
    if not shortlists:
        print(f"No shortlists found for student {student_id}.")
        return
    for shortlist in shortlists:
        position = get_position_id(shortlist.position_id)
        print(f"Shortlist ID: {shortlist.id}, Position: {position.title}, Status: {shortlist.status}, Date Added: {shortlist.date_added}")


app.cli.add_command(student_cli) # add the group to the cli


