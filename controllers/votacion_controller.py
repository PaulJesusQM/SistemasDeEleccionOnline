from flask import render_template
from domain.services.votacion_service import VotacionService

votacion_service = VotacionService()

def list_votaciones():
    votaciones = votacion_service.get_all_votaciones()
    return render_template('votacion/list.html', votaciones=votaciones)

def detail_votacion(votacion_id):
    votacion = votacion_service.get_votacion(votacion_id)
    if votacion:
        return render_template('votacion/detail.html', votacion=votacion)
    return render_template('404.html'), 404
