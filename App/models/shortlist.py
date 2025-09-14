from App.database import db
from datetime import datetime

class Shortlist(db.Model):
    __tablename__ = 'shortlists'

    id = db.Column(db.Integer, primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey('internship_position.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending') #pending, accepted, rejected
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('position_id', 'student_id', name='_position_student_uc'),)


    def __repr__(self):
        return f'<Shortlist {self.id} - Position: {self.position_id}, Student: {self.student_id}, Status: {self.status}>'