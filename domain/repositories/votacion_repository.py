from app import db
from app.domain.entities.votacion import Votacion

class VotacionRepository:
    def get_all(self):
        return Votacion.query.all()

    def get_by_id(self, id):
        return Votacion.query.get(id)
