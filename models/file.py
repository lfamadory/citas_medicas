from databases.database import db
from datetime import datetime

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    medic_id = db.Column(db.Integer, db.ForeignKey('medics.id'), nullable=False)
    details = db.Column(db.Text, nullable=True)
    
    patient = db.relationship('Patient', back_populates='files')
    medic = db.relationship('Medic', back_populates='files')

    def __init__(self, patient_id, medic_id, details):
        self.patient_id = patient_id
        self.medic_id = medic_id
        self.details = details