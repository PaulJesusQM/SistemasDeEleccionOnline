from app import db
from domain.entities.usuario import Usuario

class UsuarioRepository:
    def save(self, usuario):
        db.session.add(usuario)
        db.session.commit()
        return usuario

    def find_by_id(self, usuario_id):
        return Usuario.query.get(usuario_id)
