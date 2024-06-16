from models.user import User
from databases.database import db

class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __init__(self, account, email, password):
        super().__init__(account, email, password, 'admin')