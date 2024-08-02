from app.domain.entities.usuario import Usuario
from app.domain.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def get_all_usuarios(self):
        return self.usuario_repository.get_all()

    def get_usuario_by_id(self, id):
        return self.usuario_repository.get_by_id(id)
