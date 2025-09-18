from App.database import db
from App.models.user import User

class Employer(User):
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True, nullable=False)
    company = db.Column(db.String(100), nullable=False, default='Tech Corp')

    __mapper_args__={
        'polymorphic_identity':'employer', 
    }

    # relationship to job postings
    internship_positions = db.relationship('InternshipPosition', backref='employer', lazy=True, cascade='all, delete-orphan')

    def __init__(self, username, password, first_name, last_name, company = 'Tech Corp'):
        super().__init__(username, password, first_name, last_name)
        self.role = 'employer'
        self.company = company

    def __repr__(self):
        return f'<Employer {self.id} - {self.user.first_name} {self.user.last_name}, Company: {self.company}>'
    
    def get_json(self):
        base_json = super().get_json()
        base_json['company'] = self.company
        return base_json

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'