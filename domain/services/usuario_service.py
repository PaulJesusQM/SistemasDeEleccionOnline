from app.domain.entities.usuario import Usuario
from app.domain.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def create_usuario(self, data: dict) -> Usuario:
        usuario = Usuario(**data)
        self.repository.save(usuario)
        return usuario

    def get_usuario(self, usuario_id: int) -> Usuario:
        return self.repository.find_by_id(usuario_id)