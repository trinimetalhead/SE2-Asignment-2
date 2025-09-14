from App.database import db

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    company = db.Column(db.String(100), nullable=False)

    # relationship to job postings
    internship_positions = db.relationship('InternshipPosition', backref='employer', lazy=True, cascade='all, delete-orphan')

    def __init__(self, user_id, company):
        self.user_id = user_id
        self.company = company

    def __repr__(self):
        return f'<Employer {self.id} - {self.user.first_name} {self.user.last_name}, Company: {self.company}>'
    
    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'