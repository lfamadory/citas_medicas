from databases.database import db
from models.user import User

class UserRepository:

    @staticmethod
    def get_by_account(account):
        return User.query.filter_by(account=account).first()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def get_all_user():
        return User.query.all()
    
    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()

    @staticmethod
    def save(user):
        db.session.add(user)
        db.session.commit()

    