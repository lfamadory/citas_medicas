from models.file import File
from databases.database import db

class FileRepository:

    @staticmethod
    def get_all():
        return File.query.all()

    @staticmethod
    def get_by_id(file_id):
        return File.query.filter_by(id=file_id).first()

    @staticmethod
    def save(file):
        db.session.add(file)
        db.session.commit()

    @staticmethod
    def delete(file):
        db.session.delete(file)
        db.session.commit()