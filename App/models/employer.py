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

#CREATE
    def __init__(self, username, password, first_name, last_name, company = 'Tech Corp'):
        super().__init__(username, password, first_name, last_name)
        self.role = 'employer'
        self.company = company

#READ
    def __repr__(self):
        return f'<Employer {self.id} - {self.first_name} {self.last_name}, Company: {self.company}>'
    
    def get_json(self):
        base_json = super().get_json()
        base_json['company'] = self.company
        return base_json

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
#UPDATE
    def update_company(self, new_company):
        self.company = new_company
        db.session.commit()

#DELETE
    #Handled by cascade user model