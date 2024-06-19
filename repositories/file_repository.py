from models.file import File
from databases.database import db

class FileRepository:

    @staticmethod
    def save(file):
        db.session.add(file)
        db.session.commit()

    @staticmethod
    def get_by_id(file_id):
        return File.query.get(file_id)

    @staticmethod
    def delete(file):
        db.session.delete(file)
        db.session.commit()

    @staticmethod
    def get_all():
        return File.query.all()

    @staticmethod
    def update():
        db.session.commit()