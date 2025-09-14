from App.database import db 

class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    position = db.Column(db.String(50), nullable=False) #e.g. lecturer, admin

    def init__(self, user_id, position):
        self.user_id = user_id
        self.position = position

    def __repr__(self):
        return f'<Staff {self.id} - {self.user.first_name} {self.user.last_name}, Position: {self.position}>'
    
    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
