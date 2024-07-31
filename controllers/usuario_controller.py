from flask import Blueprint, request, jsonify
from domain.services.usuario_service import UsuarioService

usuario_bp = Blueprint('usuario_bp', __name__)
usuario_service = UsuarioService()

@usuario_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    new_usuario = usuario_service.create_usuario(data)
    return jsonify(new_usuario), 201

@usuario_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = usuario_service.get_usuario(id)
    if usuario:
        return jsonify(usuario), 200
    return jsonify({"error": "Usuario not found"}), 404
