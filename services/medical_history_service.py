from repositories.medical_history_repository import MedicalHistoryRepository
from models.medical_history import MedicalHistory

class MedicalHistoryService:

    @staticmethod
    def add_medical_history(patient_id, medic_id, diagnosis, treatment, notes=None):
        history = MedicalHistory(patient_id=patient_id, medic_id=medic_id, diagnosis=diagnosis, treatment=treatment, notes=notes)
        MedicalHistoryRepository.save(history)
        return {'message': 'Medical history added successfully'}, 201

    @staticmethod
    def get_medical_history_by_patient_and_medic(patient_id, medic_id):
        histories = MedicalHistoryRepository.get_by_patient_and_medic(patient_id, medic_id)
        return [{'id': h.id, 'visit_date': h.visit_date, 'diagnosis': h.diagnosis, 'treatment': h.treatment, 'notes': h.notes} for h in histories]

    @staticmethod
    def get_all_medical_history_by_patient(patient_id):
        histories = MedicalHistoryRepository.get_all_by_patient(patient_id)
        return [{'id': h.id, 'visit_date': h.visit_date, 'diagnosis': h.diagnosis, 'treatment': h.treatment, 'notes': h.notes} for h in histories]