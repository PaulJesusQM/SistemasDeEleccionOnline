#-*- coding: utf-8 -*-

from django.db import models

class VotoServicioDominio(models.Model):
    class Meta:
        pass

    def registrarVoto(self, voto):
        pass

    def anularVoto(self, votoId):
        pass

    def contarVotosPorEleccion(self, eleccionId):
        pass

