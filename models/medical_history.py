from databases.database import db
from datetime import datetime
from models.patient import Patient
from models.medic import Medic

class MedicalHistory(db.Model):
    __tablename__ = 'medical_histories'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    medic_id = db.Column(db.Integer, db.ForeignKey('medics.id'), nullable=False)
    visit_date = db.Column(db.DateTime, default=datetime.utcnow)
    diagnosis = db.Column(db.String(255), nullable=False)
    treatment = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.Text, nullable=True)

    patient = db.relationship('Patient', back_populates='medical_histories')
    medic = db.relationship('Medic', back_populates='medical_histories')

Patient.medical_histories = db.relationship('MedicalHistory', order_by=MedicalHistory.id, back_populates='patient')
Medic.medical_histories = db.relationship('MedicalHistory', order_by=MedicalHistory.id, back_populates='medic')