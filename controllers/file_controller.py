from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.file_service import FileService
from models.patient import Patient

file_blueprint = Blueprint('files', __name__)

@file_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_file():
    data = request.get_json()
    current_user = get_jwt_identity()
    patient = Patient.query.filter_by(id=current_user['id']).first()

    if not patient:
        return jsonify({'message': 'Patient not found'}), 404

    response, status_code = FileService.create_file(
        patient,
        data['medic_id'],
        data['details'],
        data['presentation_time']
    )
    return jsonify(response), status_code



@file_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_all_files():
    result, status_code = FileService.get_all_files()
    return jsonify(result), status_code

@file_blueprint.route('/<int:file_id>', methods=['GET'])
@jwt_required()
def get_file_by_id(file_id):
    result, status_code = FileService.get_file_by_id(file_id)
    return jsonify(result), status_code



@file_blueprint.route('/<int:file_id>', methods=['PUT'])
@jwt_required()
def update_file(file_id):
    data = request.get_json()
    response, status_code = FileService.update_file(file_id, data)
    return jsonify(response), status_code

@file_blueprint.route('/<int:file_id>', methods=['DELETE'])
@jwt_required()
def delete_file(file_id):
    response, status_code = FileService.delete_file(file_id)
    return jsonify(response), status_code