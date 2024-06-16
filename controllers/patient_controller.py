from flask import Blueprint, request, jsonify
from services.patient_service import PatientService
from flask_jwt_extended import jwt_required

patient_blueprint = Blueprint('patients', __name__)

@patient_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_patient():
    data = request.get_json()
    return PatientService.create_patient(data['account'], data['email'], data['password'], data['name'], data['last_name'], data['birthdate'], data['sex'], data['phone_number'])

@patient_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_all_patients():
    return PatientService.get_all_patients()

@patient_blueprint.route('/<int:patient_id>', methods=['GET'])
@jwt_required()
def get_patient_by_id(patient_id):
    return PatientService.get_patient_by_id(patient_id)

@patient_blueprint.route('/<int:patient_id>', methods=['DELETE'])
@jwt_required()
def delete_patient(patient_id):
    return PatientService.delete_patient(patient_id)

@patient_blueprint.route('/<int:patient_id>', methods=['PUT'])
@jwt_required()
def update_patient(patient_id):
    data = request.get_json()
    result, status_code = PatientService.update_patient(patient_id, data)
    return jsonify(result), status_code