from app import db
from domain.entities.votacion import Votacion

class VotacionRepository:
    def save(self, votacion):
        db.session.add(votacion)
        db.session.commit()
        return votacion

    def find_by_id(self, votacion_id):
        return Votacion.query.get(votacion_id)
