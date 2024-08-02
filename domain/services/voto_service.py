from app.domain.entities.voto import Voto
from app.domain.repositories.voto_repository import VotoRepository

class VotoService:
    def __init__(self):
        self.voto_repository = VotoRepository()

    def get_all_votos(self):
        return self.voto_repository.get_all()

    def get_voto_by_id(self, id):
        return self.voto_repository.get_by_id(id)
