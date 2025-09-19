from App.database import db
from datetime import datetime

class Shortlist(db.Model):
    __tablename__ = 'shortlists'

    id = db.Column(db.Integer, primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey('internship_position.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    staff_id =db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #the staff member who shortlisted the student
    status = db.Column(db.String(20), nullable=False, default='pending') #pending, accepted, rejected
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('position_id', 'student_id', name='_position_student_uc'),)

#CREATE
    def __init__(self,staff_id,  position_id, student_id):
        self.staff_id = staff_id
        self.position_id = position_id
        self.student_id = student_id

#READ     
    def get_json(self):
        return {
            'id': self.id,
            'position_id': self.position_id,
            'student_id': self.student_id,
            'staff_id': self.staff_id,
            'status': self.status,
            'date_added': self.date_added.isoformat()
        }

    def __repr__(self):
        return f'<Shortlist {self.id} - Position: {self.position_id}, Student: {self.student_id}, Status: {self.status}>'
    

#UPDATE

    def update_status(self, new_status):
        if new_status in ['pending', 'accepted', 'rejected']:
            self.status = new_status
            db.session.commit()
            return True
        return False
    
    def update_date_added(self, new_date):
        self.date_added = new_date
        db.session.commit()
        return True
    
    
    
#DELETE 
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True
    

    def accept(self):
        self.status = 'accepted'
        db.session.commit()
    
    def reject(self):
        self.status = 'rejected'
        db.session.commit()



        