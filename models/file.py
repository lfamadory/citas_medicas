from datetime import datetime
from databases.database import db

class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    medic_id = db.Column(db.Integer, db.ForeignKey('medics.id'), nullable=False)
    details = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(50), default='pendiente')
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    presentation_time = db.Column(db.DateTime, nullable=False)

    patient = db.relationship('Patient', back_populates='files')
    medic = db.relationship('Medic', back_populates='files')