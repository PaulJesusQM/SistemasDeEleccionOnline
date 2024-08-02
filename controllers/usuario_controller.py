from flask import Blueprint, request, jsonify
from app import db
from app.domain.entities.usuario import Usuario
from app.domain.services.usuario_service import UsuarioService

usuario_controller = Blueprint('usuario_controller', __name__)
usuario_service = UsuarioService()

@usuario_controller.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = usuario_service.get_all_usuarios()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@usuario_controller.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = usuario_service.get_usuario_by_id(id)
    if usuario is None:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    return jsonify(usuario.to_dict())
