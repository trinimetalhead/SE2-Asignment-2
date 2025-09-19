from App.models import Shortlist
from App.database import db
from App.controllers.user import get_user
from App.controllers.internship import get_position_id 

#CREATE

def add_to_shortlist(staff_id, student_id, position_id):
    #heck is staff exisits
    staff = get_user(staff_id)
    if not staff:
        raise ValueError(f"Staff with ID: {staff_id} does not exist")
    #Check if student exisits
    student = get_user(student_id)
    if not student:
        raise ValueError(f"Staff with ID: {student_id} does not exist")
    #Check if position is real
    position = get_position_id(position_id)
    if not position:
        raise ValueError(f"Position {position_id} does not exist")
    
    #Check if already shortlisted
    existing_shortlist = Shortlist.query.filter_by(position_id=position_id, student_id=student_id).first()
    if existing_shortlist:
        raise ValueError(f"Student {student_id} is already shortlisted for position {position_id}")
    
    newShortlist = Shortlist(staff_id, position_id, student_id)
    db.session.add(newShortlist)
    db.session.commit()
    return newShortlist

#READ 

def get_shortlist_id(shortlist_id):
    return Shortlist.query.get(shortlist_id)

def get_all_shortlists():
    return Shortlist.query.all()

def get_shortlists_student(student_id):
    return Shortlist.query.filter_by(student_id=student_id).all()

def get_shoetlis_position(position_id):
    return Shortlist.query.filter_by(positon_id=position_id).all()

def get_shortlists_staff(staff_id):
    return Shortlist.query.filter_by(staff_id=staff_id).all()

def get_shortlists_date(date):
    return Shortlist.query.filter_by(date=date).all()

#UPDATE 

def update_shortlist_status(shortlist_id, new_status):
    shortlist = get_shortlist_id(shortlist_id)
    if not shortlist:
        raise ValueError(f"Shortlist {shortlist_id} does not exist")
    if shortlist.update_status(new_status):
        return shortlist
    

#DELETE
def delete_shortlist(shortlist_id):
    shortlist = get_shortlist_id(shortlist_id)
    if not shortlist:
        raise ValueError(f"Shortlist {shortlist_id} does not exist")
    else: 
        shortlist.delete()

