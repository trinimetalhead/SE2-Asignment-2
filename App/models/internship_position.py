from App.database import db

class InternshipPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)   
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime, default=db.func.current_timestamp())
    

    #relationship to shortlist 
    shortlists = db.relationship('Shortlist', backref='internship_position', lazy=True, cascade='all, delete-orphan')
#CREATE

    def __init__(self, title, description,requirements, employer_id):
        self.title = title
        self.description = description
        self.requirements = requirements
        self.employer_id = employer_id
        self.date_posted = db.func.current_timestamp()
    
#READ

    def get_shoetlist(self):
        return self.shortlists

    def __repr__(self):
        return f'<InternshipPosition {self.id} - {self.title} - crated on {self.date_posted}>'
    
    def get_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'requirements': self.requirements,
            'employer_id': self.employer_id
        }
    
#UPDATE 
    def get_shoetlist(self):
        return self.shortlists
    
    def update_title(self, new_title):
        self.title = new_title
        self.date_posted = db.func.current_timestamp()
        db.session.commit()
    
    def update_description(self, new_description):
        self.description = new_description
        self.date_posted = db.func.current_timestamp()
        db.session.commit()

    def update_requirements(self, new_requirements):
        self.requirements = new_requirements
        self.date_posted = db.func.current_timestamp()
        db.session.commit()

    #DELETE
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True