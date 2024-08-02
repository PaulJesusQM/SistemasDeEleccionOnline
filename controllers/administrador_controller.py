from flask import Blueprint, request, jsonify
from app.domain.services.administrador_service import AdministradorService

administrador_controller = Blueprint('administrador_controller', __name__)
administrador_service = AdministradorService()

@administrador_controller.route('/administradores', methods=['GET'])
def get_administradores():
    administradores = administrador_service.get_all_administradores()
    return jsonify([administrador.to_dict() for administrador in administradores])

@administrador_controller.route('/administradores/<int:id>', methods=['GET'])
def get_administrador(id):
    administrador = administrador_service.get_administrador_by_id(id)
    if administrador is None:
        return jsonify({'error': 'Administrador no encontrado'}), 404
    return jsonify(administrador.to_dict())
