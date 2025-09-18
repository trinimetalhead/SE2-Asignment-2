from App.database import db 
from App.models.user import User

class Student(User):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'),primary_key=True, nullable=False)
    major = db.Column(db.String(50), nullable=False, default='Undeclared')

    __mapper_args__={
        'polymorphic_identity':'student',
    }

#CREATE

    def __init__(self, username, password, first_name, last_name, major = 'Undeclared'):
        super().__init__(username, password, first_name, last_name)
        self.role = 'student'
        self.major = major

#READ
    def __repr__(self):
        return f'<Student {self.id} - {self.first_name} {self.last_name}, Major: {self.major}>'

    def get_json(self):
        base_json = super().get_json()
        base_json['major'] = self.major
        return base_json
    
#UPDATE
    def update_major(self, new_major):
        self.major = new_major
        db.session.commit()

#DELETE
    #cascade delete handled by relationship in user model