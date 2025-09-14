from App.database import db

class InternshipPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)

    #relationship to shortlist 
    shortlists = db.relationship('Shortlist', backref='internship_position', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<InternshipPosition {self.id} - {self.title}>'
    
    def get_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'employer_id': self.employer_id
        }