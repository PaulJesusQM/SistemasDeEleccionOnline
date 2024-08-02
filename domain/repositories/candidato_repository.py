from app import db
from app.domain.entities.candidato import Candidato

class CandidatoRepository:
    def get_all(self):
        return Candidato.query.all()

    def get_by_id(self, id):
        return Candidato.query.get(id)
