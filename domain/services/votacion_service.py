from domain.entities.votacion import Votacion
from domain.repositories.votacion_repository import VotacionRepository

class VotacionService:
    def __init__(self):
        self.votacion_repository = VotacionRepository()

    def create_votacion(self, data):
        votacion = Votacion(
            titulo=data['titulo'],
            descripcion=data['descripcion'],
            fecha_inicio=data['fecha_inicio'],
            fecha_fin=data['fecha_fin']
        )
        return self.votacion_repository.save(votacion)

    def get_votacion(self, votacion_id):
        return self.votacion_repository.find_by_id(votacion_id)
