from repositories.user_repository import UserRepository
from models.admin import Admin

class AdminService:

    @staticmethod
    def create_admin(account, email, password, name, last_name):
        admin = Admin(account=account, email=email, password=password, name=name, last_name=last_name)
        UserRepository.save(admin)
        return {'message': 'Admin created successfully'}, 201

    @staticmethod
    def get_all_users():
        users = UserRepository.get_all()
        return [{'id': user.id, 'account': user.account, 'email': user.email, 'role': user.role} for user in users], 200

    @staticmethod
    def get_user_by_id(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            return {'id': user.id, 'account': user.account, 'email': user.email, 'role': user.role}, 200
        return {'message': 'User not found'}, 404

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            UserRepository.delete(user)
            return {'message': 'User deleted successfully'}, 200
        return {'message': 'User not found'}, 404