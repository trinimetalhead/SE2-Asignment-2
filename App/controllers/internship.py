from App.models import InternshipPosition, Shortlist, Student, Employer
from App.database import db
def create_internship_position(employer_id, title, description, requirements):
    #check if employer exisits
    employer = Employer.query.get(employer_id)
    if not employer:
        raise ValueError("This Employer does not exist or Incorrect employer ID")
    
    position = InternshipPosition(title=title, description=description, requirements=requirements, employer_id=employer_id)
    db.session.add(position)
    db.session.commit()
    return position


def get_position_id(position_id):
    return InternshipPosition.query.get(position_id)

def get_all_positions():
    return InternshipPosition.query.all()

def get_positions_by_employer(employer_id):
    return InternshipPosition.query.filter_by(employer_id=employer_id).all()



def update_position_title(position_id,title):
    position = get_position_id(position_id)
    if position:
        position.update_title(title)
        return print(f"Position {position_id} title update {title}")
    return print(f"Position Not Found with id {position_id}")

def update_position_description(position_id,description):
    position = get_position_id(position_id)
    if position:
        position.update_description(description)
        return print(f"Position {position_id} {position.title} description updated to {description}")
    return print(f"Position Not Found with id {position_id}")

def update_position_requirements(position_id,requirements):
    position = get_position_id(position_id)
    if position:
        position.update_requirements(requirements)
        return print(f"Position {position_id}: requirements updated {requirements}")
    return print(f"Position Not Found with id {position_id}")

def delete_position(position_id):
    position = get_position_id(position_id)
    if position:
        position.delete()
        return print(f"Position {position_id} Deleted.")


def update_positon(position_id, **kwargs):
    position = get_position_id(position_id)
    if position:
        return position.update(**kwargs)
    return print(f"Position {position_id}not found.")




""" def get_internships_by_employer(employer_id):
    return InternshipPosition.query.filter_by(employer_id=employer_id).all()

def get_internship_shortlists(position_id):
    return Shortlist.query.filter_by(position_id=position_id).all()

def accept_student(position_id):
    shortlist = Shortlist.query.get(position_id)
    if shortlist:
        shortlist.accept()
        return True
    return False

def reject_student(position_id):
    shortlist = Shortlist.query.get(position_id)
    if shortlist:
        shortlist.reject()
        return True
    return False

def reject_all_other_students(position_id, accepted_student_id):
    #reject all other students when one student is accepted
    shortlists = Shortlist.query.filter(Shortlist.position_id == position_id,
                                            Shortlist.student_id != accepted_student_id).all()
    for shortlist in shortlists:
        shortlist.status = 'rejected'
    db.session.commit()
    
    return len(shortlists) """