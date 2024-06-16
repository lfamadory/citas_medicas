from models.patient import Patient
from databases.database import db

class PatientRepository:

    @staticmethod
    def get_all():
        return Patient.query.all()

    @staticmethod
    def get_by_id(patient_id):
        return Patient.query.filter_by(id=patient_id).first()

    @staticmethod
    def save(patient):
        db.session.add(patient)
        db.session.commit()

    @staticmethod
    def delete(patient):
        db.session.delete(patient)
        db.session.commit()