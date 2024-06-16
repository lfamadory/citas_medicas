from repositories.user_repository import UserRepository
from models.user import User
from models.patient import Patient
from models.medic import Medic
from models.admin import Admin
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class AuthService:

    @staticmethod
    def register_user(account, email, password, role, validation_code=None):
        if UserRepository.get_by_account(account) or UserRepository.get_by_email(email):
            return {'message': 'User already exists'}, 409

        if role in ['medic', 'admin'] and validation_code != '12':
            return {'message': 'Invalid validation code'}, 403

        hashed_password = generate_password_hash(password).decode('utf-8')
        
        if role == 'patient':
            user = Patient(account=account, email=email, password=hashed_password)
        elif role == 'medic':
            user = Medic(account=account, email=email, password=hashed_password)
        elif role == 'admin':
            user = Admin(account=account, email=email, password=hashed_password)
        
        UserRepository.save(user)
        return {'message': 'User created successfully. Please complete your profile.'}, 201

    @staticmethod
    def complete_profile(user_id, **kwargs):
        user = UserRepository.get_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404

        for key, value in kwargs.items():
            setattr(user, key, value)

        UserRepository.save(user)
        return {'message': 'Profile updated successfully'}, 200

    @staticmethod
    def login_user(account, password):
        user = UserRepository.get_by_account(account)
        if not user or not check_password_hash(user.password, password):
            return {'message': 'Invalid credentials'}, 401

        access_token = create_access_token(identity={'account': user.account, 'role': user.role})
        return {'access_token': access_token}, 200