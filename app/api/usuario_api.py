from flask import Blueprint, jsonify, request
from app import db
from domain.entities.usuario import Usuario

usuario_api = Blueprint('usuario_api', __name__)

@usuario_api.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@usuario_api.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    usuario = Usuario(nombre=data['nombre'], email=data['email'], password=data['password'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify(usuario.to_dict()), 201
