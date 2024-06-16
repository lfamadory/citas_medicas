from repositories.file_repository import FileRepository
from models.file import File
from datetime import datetime, timedelta

class FileService:

    @staticmethod
    def create_file(patient_id, medic_id, details):
        file = File(patient_id=patient_id, medic_id=medic_id, details=details)
        FileRepository.save(file)
        return {'message': 'File created successfully'}, 201

    @staticmethod
    def get_all_files():
        files = FileRepository.get_all()
        return [{'id': fl.id, 'creation_date': fl.creation_date, 'patient_id': fl.patient_id, 'medic_id': fl.medic_id, 'details': fl.details} for fl in files], 200

    @staticmethod
    def get_file_by_id(file_id):
        file = FileRepository.get_by_id(file_id)
        if file:
            return {'id': file.id, 'creation_date': file.creation_date, 'patient_id': file.patient_id, 'medic_id': file.medic_id, 'details': file.details}, 200
        return {'message': 'File not found'}, 404

    @staticmethod
    def update_file(file_id, details):
        file = FileRepository.get_by_id(file_id)
        if file and datetime.utcnow() - file.creation_date <= timedelta(minutes=15):
            file.details = details
            FileRepository.save(file)
            return {'message': 'File updated successfully'}, 200
        return {'message': 'File not found or update window has passed'}, 404

    @staticmethod
    def delete_file(file_id):
        file = FileRepository.get_by_id(file_id)
        if file:
            FileRepository.delete(file)
            return {'message': 'File deleted successfully'}, 200
        return {'message': 'File not found'}, 404