from App.database import db 

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    major = db.Column(db.String(50), nullable=False)

    #shortlist relationship
    shortlists = db.relationship('Shortlist', backref='student',lazy=True, cascade='all, delete-orphan')

    def _init__(self, user_id, major):
        self.user_id = user_id
        self.major = major

    def __repr__(self):
        return f'<Student {self.id} - {self.user.first_name} {self.user.last_name}, Major: {self.major}>'

    def get_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'major': self.major
        }

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'