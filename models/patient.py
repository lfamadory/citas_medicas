from models.user import User
from databases.database import db

class Patient(User):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    birthdate = db.Column(db.Date, nullable=True)
    sex = db.Column(db.String(10), nullable=True)
    phone_number = db.Column(db.String(20), nullable=True)

    files = db.relationship('File', back_populates='patient')

    __mapper_args__ = {
        'polymorphic_identity': 'patient',
    }

    def __init__(self, account, email, password):
        super().__init__(account, email, password, 'patient')