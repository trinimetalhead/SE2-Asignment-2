from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from App.models.shortlist import Shortlist

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student') #student, staff or employer


    student_shortlists = db.relationship('Shortlist',foreign_keys=Shortlist.student_id, backref='student', lazy=True, cascade='all, delete-orphan')
    staff_shortlists = db.relationship('Shortlist',foreign_keys=Shortlist.staff_id, backref='staff', lazy=True)
    
    #mapper args for polymorphic inheritance
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }

    #relationships 
    #student_profile = db.relationship('Student', backref='user', uselist=False, cascade='all, delete-orphan')
    #staff_profile = db.relationship('Staff', backref='user', uselist=False, cascade='all, delete-orphan')
    #employer_profile = db.relationship('Employer', backref='user', uselist=False, cascade='all, delete-orphan')


    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

#CREATE

    def __init__(self, username, password, first_name, last_name):
        self.username = username
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name


#READ

    def __repr__(self):
        return f'<User {self.id} - {self.username}, Role: {self.role}>'

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role
        }
    
#UPDATE
    def update_username(self, new_username):
        self.username = new_username
        return True

    def update_firstname(self, new_first_name):
        self.first_name = new_first_name
        return True

    def update_lastname(self, new_last_name):
        self.last_name = new_last_name
        return True

    def update_password(self, new_password):
        self.set_password(new_password)
        return True


    #DELETE
    def delete(self):
        db.session.delete(self)
        db.session.commit()


    

