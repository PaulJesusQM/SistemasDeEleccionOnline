from flask import Blueprint, request, jsonify
from app.domain.services.usuario_service import UsuarioService
from app.domain.repositories.usuario_repository import UsuarioRepository

usuario_bp = Blueprint('usuario_bp', __name__)

usuario_repository = UsuarioRepository()
usuario_service = UsuarioService(usuario_repository)

@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    usuario = usuario_service.create_usuario(data)
    return jsonify(usuario.serialize()), 201

@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    usuario = usuario_service.get_usuario(usuario_id)
    if usuario is not None:
        return jsonify(usuario.serialize()), 200
    return jsonify({"error": "Usuario no encontrado"}), 404
