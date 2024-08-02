from flask import Blueprint, request, jsonify
from app.domain.services.votacion_service import VotacionService

votacion_controller = Blueprint('votacion_controller', __name__)
votacion_service = VotacionService()

@votacion_controller.route('/votaciones', methods=['GET'])
def get_votaciones():
    votaciones = votacion_service.get_all_votaciones()
    return jsonify([votacion.to_dict() for votacion in votaciones])

@votacion_controller.route('/votaciones/<int:id>', methods=['GET'])
def get_votacion(id):
    votacion = votacion_service.get_votacion_by_id(id)
    if votacion is None:
        return jsonify({'error': 'Votación no encontrada'}), 404
    return jsonify(votacion.to_dict())
