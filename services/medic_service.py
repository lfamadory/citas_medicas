from repositories.medic_repository import MedicRepository
from models.medic import Medic
from databases.database import db

class MedicService:

#Aun no se decide si se hace create
    @staticmethod
    def create_medic(account, email, password, name, last_name, speciality):
        medic = Medic(account=account, email=email, password=password, name=name, last_name=last_name, speciality=speciality)
        MedicRepository.save(medic)
        return {'message': 'Medic created successfully'}, 201

    @staticmethod
    def get_all_medics():
        medics = MedicRepository.get_all()
        return [{'id': md.id, 'name': md.name, 'last_name': md.last_name, 'speciality': md.speciality} for md in medics], 200

    @staticmethod
    def get_medic_by_id(medic_id):
        medic = MedicRepository.get_by_id(medic_id)
        if medic:
            return {'id': medic.id, 'name': medic.name, 'last_name': medic.last_name, 'specialty': medic.speciality}, 200
        return {'message': 'Medic not found'}, 404
    
    @staticmethod
    def update_medic(medic_id, data):
        medic = Medic.query.get(medic_id)
        if not medic:
            return {'message': 'Medic not found'}, 404
        
        # Actualiza los campos del paciente con los datos recibidos
        medic.name = data.get('name', medic.name)
        medic.last_name = data.get('last_name', medic.last_name)
        medic.speciality = data.get('speciality', medic.speciality)
        
        # Guarda los cambios en la base de datos
        db.session.commit()
        
        return {'message': 'Medic updated successfully'}, 200
    

    #Aun no se decide si se hace delete 
    @staticmethod
    def delete_medic(medic_id):
        medic = MedicRepository.get_by_id(medic_id)
        if medic:
            MedicRepository.delete(medic)
            return {'message': 'Medic deleted successfully'}, 200
        return {'message': 'Medic not found'}, 404
    
    