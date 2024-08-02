from flask import Blueprint, request, jsonify
from app.domain.services.voto_service import VotoService

voto_controller = Blueprint('voto_controller', __name__)
voto_service = VotoService()

@voto_controller.route('/votos', methods=['GET'])
def get_votos():
    votos = voto_service.get_all_votos()
    return jsonify([voto.to_dict() for voto in votos])

@voto_controller.route('/votos/<int:id>', methods=['GET'])
def get_voto(id):
    voto = voto_service.get_voto_by_id(id)
    if voto is None:
        return jsonify({'error': 'Voto no encontrado'}), 404
    return jsonify(voto.to_dict())
