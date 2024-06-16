from flask import Blueprint, request, jsonify
from services.file_service import FileService
from flask_jwt_extended import jwt_required

file_blueprint = Blueprint('files', __name__)

@file_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_file():
    data = request.get_json()
    return FileService.create_file(data['patient_id'], data['medic_id'], data['details'])

@file_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_all_files():
    return FileService.get_all_files()

@file_blueprint.route('/<int:file_id>', methods=['GET'])
@jwt_required()
def get_file_by_id(file_id):
    return FileService.get_file_by_id(file_id)

@file_blueprint.route('/<int:file_id>', methods=['PUT'])
@jwt_required()
def update_file(file_id):
    data = request.get_json()
    return FileService.update_file(file_id, data['details'])

@file_blueprint.route('/<int:file_id>', methods=['DELETE'])
@jwt_required()
def delete_file(file_id):
    return FileService.delete_ficha(file_id)