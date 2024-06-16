from repositories.medic_repository import MedicRepository
from models.medic import Medic

class MedicService:

    @staticmethod
    def create_medic(account, email, password, name, last_name, specialty):
        medic = Medic(account=account, email=email, password=password, name=name, last_name=last_name, specialty=specialty)
        MedicRepository.save(medic)
        return {'message': 'Medic created successfully'}, 201

    @staticmethod
    def get_all_medics():
        medics = MedicRepository.get_all()
        return [{'id': md.id, 'name': md.name, 'last_name': md.last_name, 'specialty': md.specialty} for md in medics], 200

    @staticmethod
    def get_medic_by_id(medic_id):
        medic = MedicRepository.get_by_id(medic_id)
        if medic:
            return {'id': medic.id, 'name': medic.name, 'last_name': medic.last_name, 'specialty': medic.specialty}, 200
        return {'message': 'Medic not found'}, 404

    @staticmethod
    def delete_medic(medic_id):
        medic = MedicRepository.get_by_id(medic_id)
        if medic:
            MedicRepository.delete(medic)
            return {'message': 'Medic deleted successfully'}, 200
        return {'message': 'Medic not found'}, 404