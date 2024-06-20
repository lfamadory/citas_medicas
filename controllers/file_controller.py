from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.file_service import FileService
from repositories.file_repository import FileRepository
from repositories.user_repository import UserRepository  # Asegúrate de tener esto

file_blueprint = Blueprint('file', __name__)

@file_blueprint.route('/create', methods=['POST'])
@jwt_required()
def create_file():
    data = request.get_json()
    user_id = get_jwt_identity()['id']  # Asegúrate de que el JWT tiene 'id'
    current_user = UserRepository.get_by_id(user_id)  # Recupera el objeto de usuario
    if current_user.role != 'patient':
        return jsonify({'message': 'Permission denied'}), 403
    return FileService.create_file(current_user.id, data['medic_id'], data['details'], data['presentation_time'])

@file_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_all_files():
    return jsonify(FileService.get_all_files())

@file_blueprint.route('/<int:file_id>', methods=['GET'])
@jwt_required()
def get_file_by_id(file_id):
    return jsonify(FileService.get_file_by_id(file_id))

@file_blueprint.route('/<int:file_id>/update', methods=['PUT'])
@jwt_required()
def update_presentation_time(file_id):
    data = request.get_json()
    user_id = get_jwt_identity()['id']  # Asegúrate de que el JWT tiene 'id'
    current_user = UserRepository.get_by_id(user_id)  # Recupera el objeto de usuario
    return FileService.update_presentation_time(file_id, data['presentation_time'], current_user)

@file_blueprint.route('/<int:file_id>/delete', methods=['DELETE'])
@jwt_required()
def delete_file(file_id):
    user_id = get_jwt_identity()['id']  # Asegúrate de que el JWT tiene 'id'
    current_user = UserRepository.get_by_id(user_id)  # Recupera el objeto de usuario
    return FileService.delete_file(file_id, current_user)

#agenda medic
@file_blueprint.route('/agenda', methods=['GET'])
@jwt_required()
def get_appointments_by_date_range():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    user_id = get_jwt_identity()['id']
    current_user = UserRepository.get_by_id(user_id)
    if current_user.role != 'medic':
        return jsonify({'message': 'Permission denied'}), 403
    return jsonify(FileService.get_appointments_by_date_range(current_user.id, start_date, end_date))


@file_blueprint.route('/patient/pending', methods=['GET'])
@jwt_required()
def get_pending_appointments():
    current_user_id = get_jwt_identity()['id']
    pending_appointments, status_code = FileService.get_pending_appointments_by_patient(current_user_id)
    return jsonify(pending_appointments), status_code