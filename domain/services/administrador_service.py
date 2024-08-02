from app.domain.entities.administrador import Administrador
from app.domain.repositories.administrador_repository import AdministradorRepository

class AdministradorService:
    def __init__(self):
        self.administrador_repository = AdministradorRepository()

    def get_all_administradores(self):
        return self.administrador_repository.get_all()

    def get_administrador_by_id(self, id):
        return self.administrador_repository.get_by_id(id)
