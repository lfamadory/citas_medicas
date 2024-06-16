from flask import Blueprint, request, jsonify
from models.user import User
from models.patient import Patient
from models.medic import Medic
from models.admin import Admin
from databases.database import db

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
            'password':user.password,
            'email': user.email,
            'role': user.role
        }
        user_list.append(user_data)
    return jsonify({'users': user_list}), 200

#actualizar los datos de los usuarios
@user_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    if 'account' in data:
        user.account = data['account']
    if 'password' in data:
        user.password=data['password']
    if 'email' in data:
        user.email = data['email']
    if 'role' in data:
        user.role = data['role']
    
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200

# Ruta para actualizar el perfil de un paciente
@user_blueprint.route('/patient/<int:user_id>', methods=['PUT'])
def update_patient(user_id):
    data = request.get_json()
    patient = Patient.query.filter_by(id=user_id).first()
    if not patient:
        return jsonify({'message': 'Patient not found'}), 404

    patient.name = data.get('name', patient.name)
    patient.last_name = data.get('last_name', patient.last_name)
    patient.birthdate = data.get('birthdate', patient.birthdate)
    patient.sex = data.get('sex', patient.sex)
    patient.phone_number = data.get('phone_number', patient.phone_number)

    db.session.commit()
    return jsonify({'message': 'Patient profile updated successfully'}), 200

# Ruta para actualizar el perfil de un médico
@user_blueprint.route('/medic/<int:user_id>', methods=['PUT'])
def update_medic(user_id):
    data = request.get_json()
    medic = Medic.query.filter_by(id=user_id).first()
    if not medic:
        return jsonify({'message': 'Medic not found'}), 404

    medic.name = data.get('name', medic.name)
    medic.last_name = data.get('last_name', medic.last_name)
    medic.speciality = data.get('speciality', medic.speciality)

    db.session.commit()
    return jsonify({'message': 'Medic profile updated successfully'}), 200

# Ruta para actualizar el perfil de un administrador
@user_blueprint.route('/admin/<int:user_id>', methods=['PUT'])
def update_admin(user_id):
    data = request.get_json()
    admin = Admin.query.filter_by(id=user_id).first()
    if not admin:
        return jsonify({'message': 'Admin not found'}), 404

    admin.name = data.get('name', admin.name)
    admin.last_name = data.get('last_name', admin.last_name)

    db.session.commit()
    return jsonify({'message': 'Admin profile updated successfully'}), 200