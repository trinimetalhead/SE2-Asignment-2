from App.models import InternshipPosition, Shortlist, Student, Employer
from App.database import db
def create_internship_position(title, description, requirements, employer_id):
    #check if employer exisits
    employer = Employer.query.get(employer_id)
    if not employer:
        raise ValueError("Employer does not exist")
    
    position = InternshipPosition(title=title, description=description, requirements=requirements, employer_id=employer_id)
    db.session.add(position)
    db.session.commit()
    return position

def get_internships_by_employer(employer_id):
    return InternshipPosition.query.filter_by(employer_id=employer_id).all()

def get_internship_shortlists(position_id):
    return Shortlist.query.filter_by(position_id=position_id).all()

def accept_student(position_id):
    shortlist = Shortlist.quesry.get(position_id)
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
    
    return len(shortlists)