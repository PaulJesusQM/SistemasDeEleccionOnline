from app import db
from app.domain.entities.usuario import Usuario

class UsuarioRepository:
    def get_all(self):
        return Usuario.query.all()

    def get_by_id(self, id):
        return Usuario.query.get(id)
