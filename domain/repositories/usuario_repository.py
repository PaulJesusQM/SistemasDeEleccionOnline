from app import db
from app.domain.entities.usuario import Usuario

class UsuarioRepository:
    def save(self, usuario: Usuario) -> None:
        db.session.add(usuario)
        db.session.commit()

    def find_by_id(self, usuario_id: int) -> Usuario:
        return Usuario.query.get(usuario_id)
