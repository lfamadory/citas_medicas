from flask import Blueprint, request, jsonify
from services.medic_service import MedicService
from flask_jwt_extended import jwt_required

medic_blueprint = Blueprint('medics', __name__)

#Aun no se decide si se hace create
@medic_blueprint.route('/', methods=['POST'])
@jwt_required()
def create_medic():
    data = request.get_json()
    return MedicService.create_medic(data['account'], data['email'], data['password'], data['name'], data['last_name'], data['specialty'])



@medic_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_all_medics():
    return MedicService.get_all_medics()

@medic_blueprint.route('/<int:medic_id>', methods=['GET'])
@jwt_required()
def get_medic_by_id(medic_id):
    return MedicService.get_medic_by_id(medic_id)

@medic_blueprint.route('/<int:medic_id>', methods=['PUT'])
@jwt_required()
def update_medic(medic_id):
    data = request.get_json()
    result, status_code = MedicService.update_medic(medic_id, data)
    return jsonify(result), status_code


#Aun no se decide si se hace delete
@medic_blueprint.route('/<int:medic_id>', methods=['DELETE'])
@jwt_required()
def delete_medic(medic_id):
    return MedicService.delete_medic(medic_id)

