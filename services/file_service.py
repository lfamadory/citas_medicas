from datetime import datetime, timedelta
from repositories.file_repository import FileRepository
from models.file import File
from models.patient import Patient
from models.medic import Medic

class FileService:

    @staticmethod
    def create_file(patient, medic_id, details, presentation_time):
        medic = Medic.query.get(medic_id)
        if not medic:
            return {'message': 'Medic not found'}, 404

        new_file = File(
            patient_id=patient.id,
            medic_id=medic.id,
            details=details,
            presentation_time=datetime.strptime(presentation_time, '%Y-%m-%dT%H:%M:%S')
        )

        FileRepository.save(new_file)

        return {
            'Patient': f"{patient.last_name} {patient.name}",
            'Medic': f"{medic.last_name} {medic.name}",
            'Specialty': medic.speciality,
            'Presentation Time': new_file.presentation_time,
            'Creation Date': new_file.creation_date,
            'Details': new_file.details,
            'State': new_file.state
        }, 201
    
    @staticmethod
    def get_all_files():
        files = FileRepository.get_all()
        return [{'id': fl.id, 'patient_name': f"{fl.patient.name} {fl.patient.last_name}", 
                 'medic_name': f"{fl.medic.name} {fl.medic.last_name}",
                 'speciality': fl.medic.speciality, 
                 'presentation_time': fl.presentation_time, 
                 'creation_date': fl.creation_date, 
                 'details': fl.details, 
                 'state': fl.state} for fl in files], 200

    @staticmethod
    def get_file_by_id(file_id):
        file = FileRepository.get_by_id(file_id)
        if file:
            return {
                'id': file.id,
                'patient_name': f"{file.patient.name} {file.patient.last_name}",
                'medic_name': f"{file.medic.name} {file.medic.last_name}",
                'speciality': file.medic.speciality,
                'presentation_time': file.presentation_time,
                'creation_date': file.creation_date,
                'details': file.details,
                'state': file.state
            }, 200
        return {'message': 'File not found'}, 404








    @staticmethod
    def update_file(file_id, data):
        file = FileRepository.get_by_id(file_id)
        if not file:
            return {'message': 'File not found'}, 404

        patient = Patient.query.get(file.patient_id)
        if datetime.utcnow() > file.creation_date + timedelta(minutes=15):
            return {'message': 'Cannot update file after 15 minutes of creation'}, 403

        if 'details' in data:
            file.details = data['details']
        if 'state' in data:
            file.state = data['state']
        
        FileRepository.update()

        return {'message': 'File updated successfully'}, 200

    @staticmethod
    def delete_file(file_id):
        file = FileRepository.get_by_id(file_id)
        if not file:
            return {'message': 'File not found'}, 404
        
        FileRepository.delete(file)

        return {'message': 'File deleted successfully'}, 200