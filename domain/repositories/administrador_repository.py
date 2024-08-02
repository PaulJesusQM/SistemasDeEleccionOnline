from app import db
from app.domain.entities.administrador import Administrador

class AdministradorRepository:
    def get_all(self):
        return Administrador.query.all()

    def get_by_id(self, id):
        return Administrador.query.get(id)
