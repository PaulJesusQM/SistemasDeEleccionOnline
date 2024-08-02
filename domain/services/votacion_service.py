from app.domain.entities.votacion import Votacion
from app.domain.repositories.votacion_repository import VotacionRepository

class VotacionService:
    def __init__(self):
        self.votacion_repository = VotacionRepository()

    def get_all_votaciones(self):
        return self.votacion_repository.get_all()

    def get_votacion_by_id(self, id):
        return self.votacion_repository.get_by_id(id)
