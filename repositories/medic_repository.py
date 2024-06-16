from models.medic import Medic
from databases.database import db

class MedicRepository:

    @staticmethod
    def get_all():
        return Medic.query.all()

    @staticmethod
    def get_by_id(medic_id):
        return Medic.query.filter_by(id=medic_id).first()

    @staticmethod
    def save(medic):
        db.session.add(medic)
        db.session.commit()

    @staticmethod
    def delete(medic):
        db.session.delete(medic)
        db.session.commit()