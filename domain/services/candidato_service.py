from app.domain.entities.candidato import Candidato
from app.domain.repositories.candidato_repository import CandidatoRepository

class CandidatoService:
    def __init__(self):
        self.candidato_repository = CandidatoRepository()

    def get_all_candidatos(self):
        return self.candidato_repository.get_all()

    def get_candidato_by_id(self, id):
        return self.candidato_repository.get_by_id(id)
