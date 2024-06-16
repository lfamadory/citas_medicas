from flask import Blueprint, request, jsonify
from models.user import User
from models.patient import Patient
from models.medic import Medic
from models.admin import Admin
from databases.database import db

user_blueprint = Blueprint('user', __name__)

# Ruta para ver todos los usuarios
@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'account': user.account,
            'password':user.password,
            'email': user.email,
            'role': user.role
        }
        user_list.append(user_data)
    return jsonify({'users': user_list}), 200

#actualizar los datos de los usuarios
@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if 'account' in data:
        user.account = data['account']
    if 'password' in data:
        user.password=data['password']
    if 'email' in data:
        user.email = data['email']
    if 'role' in data:
        user.role = data['role']
    
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

