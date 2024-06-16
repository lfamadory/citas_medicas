from flask import Blueprint, request, jsonify
from services.admin_service import AdminService
from flask_jwt_extended import jwt_required

admin_blueprint = Blueprint('admins', __name__)

@admin_blueprint.route('/create', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    role = data.get('role')
    validation_code = data.get('validation_code', None)
    return AdminService.create_user(data['account'], data['email'], data['password'], role, validation_code)



@admin_blueprint.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    return AdminService.get_all_users()

@admin_blueprint.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_by_id(user_id):
    return AdminService.get_user_by_id(user_id)



@admin_blueprint.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    data = request.get_json()
    result, status_code = AdminService.update_user(user_id, data)
    return jsonify(result), status_code


@admin_blueprint.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_users(user_id):
    return AdminService.delete_users(user_id)