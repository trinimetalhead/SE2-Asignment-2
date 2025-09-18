from App.database import db 
from App.models.user import User
class Staff(User):
    __tablename__ = 'staff'
    
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
    position = db.Column(db.String(50), nullable=False) #e.g. lecturer, admin

    __mapper_args__={
        'polymorphic_identity':'staff',
    }


    def __init__(self, username, password, first_name, last_name, position = 'Staff'):
        super().__init__(username, password, first_name, last_name)
        self.role = 'staff'
        self.position = position

    def __repr__(self):
        return f'<Staff {self.id} - {self.user.first_name} {self.user.last_name}, Position: {self.position}>'
    
    def get_json(self):
        base_jason = super().get_json()
        base_jason['position'] = self.position
        return base_jason

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
