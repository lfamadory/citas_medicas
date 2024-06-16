from repositories.user_repository import UserRepository
from models.admin import Admin
from models.patient import Patient
from models.medic import Medic
from databases.database import db
from flask_bcrypt import generate_password_hash, check_password_hash

class AdminService:

    @staticmethod
    def create_user(account, email, password, role, validation_code=None):
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
        else:
            return {'message': 'Invalid role'}, 400
        
        UserRepository.save(user)
        return {'message': f'{role.capitalize()} created successfully. Please complete your profile.'}, 201
    

    @staticmethod
    def get_all_users():
        users = UserRepository.get_all_user()
        return [{'id': user.id, 'account': user.account, 'email': user.email, 'role': user.role} for user in users], 200

    @staticmethod
    def get_user_by_id(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            return {'id': user.id, 'account': user.account, 'email': user.email, 'role': user.role}, 200
        return {'message': 'User not found'}, 404

   
    
    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_by_id(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        
        # Actualiza los campos del usuario con los datos recibidos
        user.account = data.get('account', user.account)
        if 'password' in data:
            user.password = generate_password_hash(data['password']).decode('utf-8')
        user.email = data.get('email', user.email)
        user.role = data.get('role', user.role)
        
        # Guarda los cambios en la base de datos
        UserRepository.save(user)
        
        return {'message': 'User updated successfully'}, 200
    
    @staticmethod
    def delete_users(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            UserRepository.delete_user(user)
            return {'message': 'User deleted successfully'}, 200
        return {'message': 'User not found'}, 404