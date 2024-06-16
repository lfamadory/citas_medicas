from flask import Blueprint, request, jsonify
from services.admin_service import AdminService
from flask_jwt_extended import jwt_required

admin_blueprint = Blueprint('admins', __name__)

@admin_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_admin():
    data = request.get_json()
    return AdminService.create_admin(data['account'], data['email'], data['password'], data['name'], data['last_name'])

@admin_blueprint.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    return AdminService.get_all_users()

@admin_blueprint.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    return AdminService.get_user_by_id(user_id)

@admin_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return AdminService.delete_user(user_id)