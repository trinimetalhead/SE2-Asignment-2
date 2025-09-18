import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, internship_position, Shortlist 
from App.main import create_app
from App.controllers import ( create_employer,create_staff, create_student , get_all_users_json, get_all_users, initialize, create_internship_position,
                             get_internships_by_employer)


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



#DELETE

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

@employer_cli.command("create-position", help="Creates an internship position")
@click.argument("employer_id")
@click.argument("title", default="Intern")
@click.argument("description", default="Internship position description")
@click.argument("requirements", default="3.0 GPA or Above")
def create_position(employer_id, title, description, requirements):
    positions = create_internship_position(employer_id,title,description,requirements)
    print(f"position {positions.title} created with id {positions.id}")

@employer_cli.command("list-positions", help="Lists all internship positions for an employer")
@click.argument("employer_id")
def list_positions(employer_id):
    positions = get_internships_by_employer(employer_id)
    if not positions:
        print("No positions found for this employer.")
        return
    for position in positions:
        print(f"ID: {position.id}, Title: {position.title}, Description: {position.description}, Requirements: {position.requirements}")


app.cli.add_command(employer_cli) # add the group to the cli


'''
Staff Commands
'''

staff_cli = AppGroup('staff', help='staff commands') 





app.cli.add_command(staff_cli) # add the group to the cli



