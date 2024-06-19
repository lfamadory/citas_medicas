from models.medical_history import MedicalHistory
from databases.database import db

class MedicalHistoryRepository:

    @staticmethod
    def save(history):
        db.session.add(history)
        db.session.commit()

    @staticmethod
    def get_by_patient_and_medic(patient_id, medic_id):
        return MedicalHistory.query.filter_by(patient_id=patient_id, medic_id=medic_id).all()

    @staticmethod
    def get_all_by_patient(patient_id):
        return MedicalHistory.query.filter_by(patient_id=patient_id).all()