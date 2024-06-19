from flask import Blueprint, request, jsonify
from models.user import User
from databases.database import db
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import jwt_required

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
            'email': user.email,
            'role': user.role
        }
        user_list.append(user_data)
    return jsonify({'users': user_list}), 200

# Ruta para ver un usuario por ID
@user_blueprint.route('/<int:user_id>', methods=['GET'])

def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    user_data = {
        'id': user.id,
        'account': user.account,
        'email': user.email,
        'role': user.role
    }
    return jsonify(user_data), 200

# Ruta para actualizar los datos de los usuarios
@user_blueprint.route('/<int:user_id>', methods=['PUT'])

def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if 'account' in data:
        user.account = data['account']
    if 'password' in data:
        user.password = generate_password_hash(data['password']).decode('utf-8')
    if 'email' in data:
        user.email = data['email']
    if 'role' in data:
        user.role = data['role']
    
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

# Ruta para eliminar un usuario
@user_blueprint.route('/<int:user_id>', methods=['DELETE'])

def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'}), 200