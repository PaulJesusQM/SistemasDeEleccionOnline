from flask import Blueprint, request, jsonify
from domain.services.votacion_service import VotacionService

votacion_bp = Blueprint('votacion_bp', __name__)
votacion_service = VotacionService()

@votacion_bp.route('/votaciones', methods=['POST'])
def create_votacion():
    data = request.get_json()
    new_votacion = votacion_service.create_votacion(data)
    return jsonify(new_votacion), 201

@votacion_bp.route('/votaciones/<int:id>', methods=['GET'])
def get_votacion(id):
    votacion = votacion_service.get_votacion(id)
    if votacion:
        return jsonify(votacion), 200
    return jsonify({"error": "Votacion not found"}), 404
