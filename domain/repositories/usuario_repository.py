from app import db
from app.domain.entities.usuario import Usuario
from sqlalchemy.exc import SQLAlchemyError

class UsuarioRepository:
    def save(self, usuario: Usuario):
        try:
            db.session.add(usuario)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            raise DatabaseError(f"Error saving user: {str(e)}") from e

    def find_by_id(self, usuario_id: int) -> Usuario:
        try:
            return Usuario.query.get(usuario_id)
        except SQLAlchemyError as e:
            raise DatabaseError(f"Error fetching user with ID {usuario_id}: {str(e)}") from e

class DatabaseError(Exception):
    pass
