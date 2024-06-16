from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    role = data.get('role')
    validation_code = data.get('validation_code', None)
    return AuthService.register_user(data['account'], data['email'], data['password'], role, validation_code)

@auth_blueprint.route('/complete_profile', methods=['POST'])
def complete_profile():
    data = request.get_json()
    user_id = data.get('user_id')
    profile_data = {k: v for k, v in data.items() if k != 'user_id'}
    return AuthService.complete_profile(user_id, **profile_data)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return AuthService.login_user(data['account'], data['password'])