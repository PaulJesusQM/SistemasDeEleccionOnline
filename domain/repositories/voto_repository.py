from app import db
from app.domain.entities.voto import Voto

class VotoRepository:
    def get_all(self):
        return Voto.query.all()

    def get_by_id(self, id):
        return Voto.query.get(id)
