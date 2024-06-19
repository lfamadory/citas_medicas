from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.medical_history_service import MedicalHistoryService
from repositories.user_repository import UserRepository

medical_history_blueprint = Blueprint('medical_history', __name__)

@medical_history_blueprint.route('/add', methods=['POST'])
@jwt_required()
def add_medical_history():
    data = request.get_json()
    user_id = get_jwt_identity()['id']
    current_user = UserRepository.get_by_id(user_id)
    if current_user.role != 'medic':
        return jsonify({'message': 'Permission denied'}), 403

    return jsonify(MedicalHistoryService.add_medical_history(data['patient_id'], user_id, data['diagnosis'], data['treatment'], data.get('notes')))

@medical_history_blueprint.route('/<int:patient_id>/medic', methods=['GET'])
@jwt_required()
def get_medical_history_by_patient_and_medic(patient_id):
    user_id = get_jwt_identity()['id']
    current_user = UserRepository.get_by_id(user_id)
    if current_user.role != 'medic':
        return jsonify({'message': 'Permission denied'}), 403

    return jsonify(MedicalHistoryService.get_medical_history_by_patient_and_medic(patient_id, user_id))

@medical_history_blueprint.route('/<int:patient_id>/all', methods=['GET'])
@jwt_required()
def get_all_medical_history_by_patient(patient_id):
    user_id = get_jwt_identity()['id']
    current_user = UserRepository.get_by_id(user_id)
    if current_user.role != 'medic':
        return jsonify({'message': 'Permission denied'}), 403

    return jsonify(MedicalHistoryService.get_all_medical_history_by_patient(patient_id))