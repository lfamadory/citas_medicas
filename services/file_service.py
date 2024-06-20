from repositories.file_repository import FileRepository
from models.file import File
from datetime import datetime, timedelta

class FileService:

    @staticmethod
    def create_file(patient_id, medic_id, details, presentation_time_str):
        presentation_time = datetime.fromisoformat(presentation_time_str)
        creation_date = datetime.utcnow()
        new_file = File(
            patient_id=patient_id,
            medic_id=medic_id,
            details=details,
            state='pendiente',
            creation_date=creation_date,
            presentation_time=presentation_time
        )
        FileRepository.save(new_file)
        return {'message': 'File created successfully'}, 201

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
    def update_presentation_time(file_id, new_presentation_time_str, current_user):
        file = FileRepository.get_by_id(file_id)
        if not file:
            return {'message': 'File not found'}, 404

        new_presentation_time = datetime.fromisoformat(new_presentation_time_str)

        if current_user.role == 'patient' and (datetime.utcnow() - file.creation_date > timedelta(minutes=60)):
            return {'message': 'Update not allowed after 15 minutes'}, 403

        if current_user.role == 'patient' and file.patient_id == current_user.id:
            file.presentation_time = new_presentation_time
            FileRepository.update(file)
            return {'message': 'Presentation time updated successfully'}, 200

        return {'message': 'Permission denied'}, 403

    @staticmethod
    def delete_file(file_id, current_user):
        file = FileRepository.get_by_id(file_id)
        if not file:
            return {'message': 'File not found'}, 404

        if current_user.role == 'patient' and file.patient_id == current_user.id:
            FileRepository.delete(file)
            return {'message': 'File deleted successfully'}, 200

        return {'message': 'Permission denied'}, 403
    

#mostrar gestion de agenda medic 
    @staticmethod
    def get_appointments_by_date_range(medic_id, start_date_str, end_date_str):
        start_date = datetime.fromisoformat(start_date_str)
        end_date = datetime.fromisoformat(end_date_str)
        files = FileRepository.get_by_date_range(medic_id, start_date, end_date)
        
        return [
            {
                'id': fl.id,
                'patient_name': f"{fl.patient.name} {fl.patient.last_name}",
                'medic_name': f"{fl.medic.name} {fl.medic.last_name}",
                'speciality': fl.medic.speciality,
                'presentation_time': fl.presentation_time,
                'creation_date': fl.creation_date,
                'details': fl.details,
                'state': fl.state
            } for fl in files
        ], 200
    
    @staticmethod
    def get_pending_appointments_by_patient(patient_id):
        pending_appointments = FileRepository.get_pending_appointments_by_patient(patient_id)
        return [
            {
                'id': appointment.id,
                'medic_name': f"{appointment.medic.name} {appointment.medic.last_name}",
                'speciality': appointment.medic.speciality,
                'presentation_time': appointment.presentation_time,
                'creation_date': appointment.creation_date,
                'details': appointment.details,
                'state': appointment.state
            } for appointment in pending_appointments
        ], 200