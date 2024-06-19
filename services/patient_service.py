from datetime import datetime  # Importa datetime para manejar fechas
from repositories.patient_repository import PatientRepository
from models.patient import Patient
from databases.database import db


class PatientService:

    @staticmethod
    def create_patient(account, email, password, name, last_name, birthdate, sex, phone_number):
        patient = Patient(account=account, email=email, password=password, name=name, last_name=last_name, birthdate=birthdate, sex=sex, phone_number=phone_number)
        PatientRepository.save(patient)
        return {'message': 'Patient created successfully'}, 201

    @staticmethod
    def get_all_patients():
        patients = PatientRepository.get_all()
        return [{'id': pt.id, 'name': pt.name, 'last_name': pt.last_name, 'birthdate': pt.birthdate, 'sex': pt.sex, 'phone_number': pt.phone_number} for pt in patients], 200

    @staticmethod
    def get_patient_by_id(patient_id):
        patient = PatientRepository.get_by_id(patient_id)
        if patient:
            return {'id': patient.id, 'name': patient.name, 'last_name': patient.last_name, 'birthdate': patient.birthdate, 'sex': patient.sex, 'phone_number': patient.phone_number}, 200
        return {'message': 'Patient not found'}, 404

    
    
    @staticmethod
    def update_patient(patient_id, data):
        patient = Patient.query.get(patient_id)
        if not patient:
            return {'message': 'Patient not found'}, 404
        
        # Actualiza los campos del paciente con los datos recibidos
        patient.name = data.get('name', patient.name)
        patient.last_name = data.get('last_name', patient.last_name)
        patient.sex = data.get('sex', patient.sex)
        patient.phone_number = data.get('phone_number', patient.phone_number)
        
        # Convierte la cadena de fecha de nacimiento a un objeto de fecha de Python
        try:
            if 'birthdate' in data:
                patient.birthdate = datetime.strptime(data['birthdate'], '%d-%m-%Y').date()
        except ValueError:
            return {'message': 'Invalid date format for birthdate. Use format DD-MM-YYYY.'}, 400
        
        # Guarda los cambios en la base de datos
        db.session.commit()
        
        return {'message': 'Patient updated successfully'}, 200
    

    @staticmethod
    def delete_patient(patient_id):
        patient = PatientRepository.get_by_id(patient_id)
        if patient:
            PatientRepository.delete(patient)
            return {'message': 'Patient deleted successfully'}, 200
        return {'message': 'Patient not found'}, 404