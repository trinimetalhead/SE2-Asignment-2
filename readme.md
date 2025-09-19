[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/uwidcit/flaskmvc)
<a href="https://render.com/deploy?repo=https://github.com/uwidcit/flaskmvc">
  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a>

![Tests](https://github.com/uwidcit/flaskmvc/actions/workflows/dev.yml/badge.svg)

# Flask MVC Template
A template for flask applications structured in the Model View Controller pattern [Demo](https://dcit-flaskmvc.herokuapp.com/). [Postman Collection](https://documenter.getpostman.com/view/583570/2s83zcTnEJ)


# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```

# Configuration Management


Configuration information such as the database url/port, credentials, API keys etc are to be supplied to the application. However, it is bad practice to stage production information in publicly visible repositories.
Instead, all config is provided by a config file or via [environment variables](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/).

## In Development

When running the project in a development environment (such as gitpod) the app is configured via default_config.py file in the App folder. By default, the config for development uses a sqlite database.

default_config.py
```python
SQLALCHEMY_DATABASE_URI = "sqlite:///temp-database.db"
SECRET_KEY = "secret key"
JWT_ACCESS_TOKEN_EXPIRES = 7
ENV = "DEVELOPMENT"
```

These values would be imported and added to the app in load_config() function in config.py

config.py
```python
# must be updated to inlude addtional secrets/ api keys & use a gitignored custom-config file instad
def load_config():
    config = {'ENV': os.environ.get('ENV', 'DEVELOPMENT')}
    delta = 7
    if config['ENV'] == "DEVELOPMENT":
        from .default_config import JWT_ACCESS_TOKEN_EXPIRES, SQLALCHEMY_DATABASE_URI, SECRET_KEY
        config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
        config['SECRET_KEY'] = SECRET_KEY
        delta = JWT_ACCESS_TOKEN_EXPIRES
...
```

## In Production

When deploying your application to production/staging you must pass
in configuration information via environment tab of your render project's dashboard.

![perms](./images/fig1.png)

# Flask Commands

wsgi.py is a utility script for performing various tasks related to the project. You can use it to import and test any code in the project. 
You just need create a manager command function, for example:

```python
# inside wsgi.py

user_cli = AppGroup('user', help='User object commands')

@user_cli.cli.command("create-user")
@click.argument("username")
@click.argument("password")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

app.cli.add_command(user_cli) # add the group to the cli

```

Then execute the command invoking with flask cli with command name and the relevant parameters

```bash
$ flask user create bob bobpass
```


# Running the Project

_For development run the serve command (what you execute):_
```bash
$ flask run
```

_For production using gunicorn (what the production server executes):_
```bash
$ gunicorn wsgi:app
```

# Deploying
You can deploy your version of this app to render by clicking on the "Deploy to Render" link above.

# Initializing the Database
When connecting the project to a fresh empty database ensure the appropriate configuration is set then file then run the following command. This must also be executed once when running the app on heroku by opening the heroku console, executing bash and running the command in the dyno.

```bash
$ flask init
```

# Database Migrations
If changes to the models are made, the database must be'migrated' so that it can be synced with the new models.
Then execute following commands using manage.py. More info [here](https://flask-migrate.readthedocs.io/en/latest/)

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
$ flask db --help
```

# Testing

## Unit & Integration
Unit and Integration tests are created in the App/test. You can then create commands to run them. Look at the unit test command in wsgi.py for example

```python
@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "User"]))
```

You can then execute all user tests as follows

```bash
$ flask test user
```

You can also supply "unit" or "int" at the end of the comand to execute only unit or integration tests.

You can run all application tests with the following command

```bash
$ pytest
```

## Test Coverage

You can generate a report on your test coverage via the following command

```bash
$ coverage report
```

You can also generate a detailed html report in a directory named htmlcov with the following comand

```bash
$ coverage html
```

# Troubleshooting

## Views 404ing

If your newly created views are returning 404 ensure that they are added to the list in main.py.

```python
from App.views import (
    user_views,
    index_views
)

# New views must be imported and added to this list
views = [
    user_views,
    index_views
]
```

## Cannot Update Workflow file

If you are running into errors in gitpod when updateding your github actions file, ensure your [github permissions](https://gitpod.io/integrations) in gitpod has workflow enabled ![perms](./images/gitperms.png)

## Database Issues

If you are adding models you may need to migrate the database with the commands given in the previous database migration section. Alternateively you can delete you database file.



# Command Documentation

## Firstly You Must Initialize the Database:

flask init

### This will create and populate the database with three users:
id:1 , Student, Alice_Johnson, Major=Compluter Science 
id:2 , Staff, Alice_Smith, Position=Administrator 
id:3 , Employer, Emily_Davis, Company=Tech Corp

### and two Internship Positions:
Position id: 1, Software Engineering Intern, {Description}, {Requirements}, {employer id}
Position id: 2, Data Science Intern, {Description}, {Requirements}, {employer id}


## User Commands

### Create :

flask user create-student "username" "password" "FirstName" "LastName" "Major"

flask user create-staff "username" "password" "FirstName" "LastName" "Position"

flask user create-employer "username" "password" "FirstName" "LastName" "Company"

### Read :

flask user list 
//Lists all users in the database

flask user list-staff
//lists all staff users in the database

flask user list-employers
//lists all employers users in the database

flask user list-students
//lists all students users in the database

### Update : 

flask user update-username userID "New Username"
//updates the given user's username

flask user update-first-name userID "new first name"
//updates the given user's first name 

flask user update-last-name userID "new last name"
//updates the given user's last name 

flask user update-password userID "new_password" 
//updates the given user's password 

### Delete : 

flask user delete UserID
//deletes the user with the given id

## Employer Commands 

### Create : 

flask employer create-position employerID "title" "description" "requirements"
//creates an internship position with the given arguments

### Read :

flask employer list-positions employerID
//list all the internship positions posted by the employer with ID 

flask employer view-shortlists positionID
//displays all shortlisted students for positios with ID 


### Update

flask employer update-title positionID "New Title"
//updates the title of the position with ID 

flask employer update-description positionID "New Description"
//updates the description of the position with ID 

flask employer update-requirements positionID "New Requirements"
//updates the requiremetns of the position with ID 

flask employer accept positionID studentID 
//accepts the Student with ID to the position with ID 

flask employer reject positionID studentID 
//rejects the Student with ID to the position with ID 

### Delete :

flask employer delete positionID
//deletes the posted internship position with ID 


## Staff Commands 

### Create :

flask staff add staffID studentID positionID 
//the staff with ID adds the student with ID to the internship position with ID 

### Read : 

flask staff view-positions 
//lists all internship positions

flask staff list-shortlists 
//lists all students shortlisted for all students

flask staff shortlisted-students positionID
//lists all shortlisted students for position with ID 


### Detele : 

flask staff delete shortlist_id 
//deletes shortlist entry with ID 


## Student Commands

### Read 

flask student view-shortlists studentID
//shows all positions that student with ID is shortlisted for

