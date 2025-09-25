# CLI Command Documentation

### NOTE: Controllers were used in the creation of this database

## FIrstly you must install requirements:

open your command line 'ctrl' +  ` 

```bash
$ pip install -r requirements.txt
```

## Then You Must Initialize the Database:
```bash
$ flask init
```
### This will create and populate the database with three users:
id:1 , Student, Alice_Johnson, Major=Compluter Science 

id:2 , Staff, Alice_Smith, Position=Administrator 

id:3 , Employer, Emily_Davis, Company=Tech Corp

### and two Internship Positions:
Position id: 1, Software Engineering Intern, {Description}, {Requirements}, {employer id}

Position id: 2, Data Science Intern, {Description}, {Requirements}, {employer id}


## User Commands

### Create :

```bash
$ flask user create-student "username" "password" "FirstName" "LastName" "Major"

$ flask user create-staff "username" "password" "FirstName" "LastName" "Position"

$ flask user create-employer "username" "password" "FirstName" "LastName" "Company"
```
### Read :
```bash
$ flask user list
``` 
//Lists all users in the database
```bash
$ flask user list-staff
```
//lists all staff users in the database
```bash
$ flask user list-employers
```
//lists all employers users in the database
```bash
$ flask user list-students
```
//lists all students users in the database

### Update : 

```bash
$ flask user update-username userID "New Username"
```
//updates the given user's username

```bash
$ flask user update-first-name userID "new first name"
```
//updates the given user's first name 

```bash
$ flask user update-last-name userID "new last name"
```
//updates the given user's last name 

```bash
$ flask user update-password userID "new_password" 
```
//updates the given user's password 

### Delete : 

```bash
$ flask user delete UserID
```
//deletes the user with the given id

## Employer Commands 

### Create : 

```bash
$ flask employer create-position employerID "title" "description" "requirements"
```
//creates an internship position with the given arguments

### Read :

```bash
$ flask employer list-positions employerID
```
//list all the internship positions posted by the employer with ID 

```bash
$ flask employer view-shortlists employerID positionID
```
//displays all shortlisted students for positios with ID 


### Update

```bash
$ flask employer update-title employerID positionID "New Title"
```
//updates the title of the position with ID 

```bash
$ flask employer update-description employerID positionID "New Description"
```
//updates the description of the position with ID 

```bash
$ flask employer update-requirements employerID positionID "New Requirements"
```
//updates the requiremetns of the position with ID 

```bash
$ flask employer accept employerID positionID studentID 
```
//accepts the Student with ID to the position with ID 

```bash
$ flask employer reject employerID positionID studentID 
```
//rejects the Student with ID to the position with ID 

### Delete :

```bash
$ flask employer delete employerID positionID
```
//deletes the posted internship position with ID 


## Staff Commands 

### Create :

```bash
$ flask staff add staffID studentID positionID 
```
//the staff with ID adds the student with ID to the internship position with ID 

### Read : 

```bash
$ flask staff view-positions staffID
```
//lists all internship positions

```bash
$ flask staff list-shortlists staffID
```
//lists all students shortlisted for all students

```bash
$ flask staff shortlisted-students staffID positionID
```
//lists all shortlisted students for position with ID 


### Delete : 

```bash
$ flask staff delete staff_id shortlist_id
```
//deletes shortlist entry with ID 


## Student Commands

### Read 

```bash
$ flask student view-shortlists studentID studentID
```
//shows all positions that student with ID is shortlisted for

