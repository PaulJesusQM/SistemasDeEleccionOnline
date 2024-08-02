from flask import Blueprint, request, jsonify
from app.domain.services.candidato_service import CandidatoService

candidato_controller = Blueprint('candidato_controller', __name__)
candidato_service = CandidatoService()

@candidato_controller.route('/candidatos', methods=['GET'])
def get_candidatos():
    candidatos = candidato_service.get_all_candidatos()
    return jsonify([candidato.to_dict() for candidato in candidatos])

@candidato_controller.route('/candidatos/<int:id>', methods=['GET'])
def get_candidato(id):
    candidato = candidato_service.get_candidato_by_id(id)
    if candidato is None:
        return jsonify({'error': 'Candidato no encontrado'}), 404
    return jsonify(candidato.to_dict())
