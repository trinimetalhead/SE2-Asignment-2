import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )


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
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("first_name", default="Rob")
@click.argument("last_name", default="Smith")
@click.argument("role", default="student")
@click.argument("extra", default='') # for any extra info like major, position, company
def create_user_command(username, password, first_name, last_name, role, extra):
    if role == 'student':
        create_user(username, password, first_name, last_name, role, major=extra)
    elif role == 'staff':
        create_user(username, password, first_name, last_name, role, position=extra)
    elif role == 'employer':
        create_user(username, password, first_name, last_name, role, company=extra)
    
    print(f'{username} created with the role of {role}!')

# this command will be : flask user create bob bobpass

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
        print(f"ID: {user.id}, Username: {user.username}, Name: {user.first_name} {user.last_name}, Position: {user.staff_profile.position}")

@user_cli.command("list-employers", help="Lists all employer users in the database")
def list_employers_command():
    employers = [user for user in get_all_users() if user.role == 'employer']
    if not employers:
        print("No employer users found.")
        return
    for user in employers:
        print(f"ID: {user.id}, Username: {user.username}, Name: {user.first_name} {user.last_name}, Company: {user.employer_profile.company}")

@user_cli.command("list-students", help="Lists all student users in the database")
def list_students_command():
    students = [user for user in get_all_users() if user.role == 'student']
    if not students:
        print("No student users found.")
        return
    for user in students:
        print(f"ID: {user.id}, Username: {user.username}, Name: {user.first_name} {user.last_name}, Major: {user.student_profile.major}")

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