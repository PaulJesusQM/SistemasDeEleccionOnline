from domain.entities.usuario import Usuario
from domain.repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.usuario_repository = UsuarioRepository()

    def create_usuario(self, data):
        usuario = Usuario(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )
        return self.usuario_repository.save(usuario)

    def get_usuario(self, usuario_id):
        return self.usuario_repository.find_by_id(usuario_id)
