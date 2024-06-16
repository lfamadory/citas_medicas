from models.user import User
from databases.database import db

class Medic(User):
    __tablename__ = 'medics'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    speciality = db.Column(db.String(100), nullable=True)

    files = db.relationship('File', back_populates='medic')

    __mapper_args__ = {
        'polymorphic_identity': 'medic',
    }

    def __init__(self, account, email, password):
        super().__init__(account, email, password, 'medic')