from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student') #student, staff or employer

    #relationships 
    student_profile = db.relationship('Student', backref='user', uselist=False, cascade='all, delete-orphan')
    staff_profile = db.relationship('Staff', backref='user', uselist=False, cascade='all, delete-orphan')
    employer_profile = db.relationship('Employer', backref='user', uselist=False, cascade='all, delete-orphan')

    def __init__(self, username, password, first_name, last_name, role):
        self.username = username
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

        # validate role 
        if role not in ['student', 'staff', 'employer']:
            raise ValueError("Role must be 'student', 'staff', or 'employer'")

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    
    #helper methods 

    def is_student(self):
        return self.role == 'student'
    def is_staff(self):
        return self.role == 'staff'
    def is_employer(self):
        return self.role == 'employer'

