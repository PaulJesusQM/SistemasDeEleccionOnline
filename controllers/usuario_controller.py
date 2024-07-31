from flask import Blueprint, request, jsonify
from app.domain.services.usuario_service import UsuarioService
from app.domain.repositories.usuario_repository import UsuarioRepository

usuario_bp = Blueprint('usuario_bp', __name__)
usuario_repository = UsuarioRepository()
usuario_service = UsuarioService(usuario_repository)

@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    try:
        usuario = usuario_service.create_usuario(data)
        return jsonify(usuario.serialize()), 201
    except DatabaseError as e:
        return jsonify({"error": str(e)}), 400

@usuario_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    try:
        usuario = usuario_service.get_usuario(usuario_id)
        if usuario:
            return jsonify(usuario.serialize()), 200
        else:
            return jsonify({"error": "Usuario no encontrado"}), 404
    except DatabaseError as e:
        return jsonify({"error": str(e)}), 400
