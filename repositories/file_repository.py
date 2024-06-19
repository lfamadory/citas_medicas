from models.file import File
from databases.database import db

class FileRepository:

    @staticmethod
    def save(file):
        db.session.add(file)
        db.session.commit()

    @staticmethod
    def get_all():
        return File.query.all()

    @staticmethod
    def get_by_id(file_id):
        return File.query.get(file_id)

    @staticmethod
    def update(file):
        db.session.commit()
    
    @staticmethod
    def delete(file):
        db.session.delete(file)
        db.session.commit()

#agenda medic
    @staticmethod
    def get_by_date_range(medic_id, start_date, end_date):
        return File.query.filter(
            File.medic_id == medic_id,
            File.presentation_time >= start_date,
            File.presentation_time <= end_date
        ).all()