#-*- coding: utf-8 -*-

from django.db import models

class Elector(models.Model):
    class Meta:
        pass

    id = undefined()
    nombre = undefined()
    credenciales = undefined()
    String password = None


    def emitirVoto(self, String eleccionId, String candidatoId):
        pass

    def verificarVoto(self, String eleccionId):
        pass

    def haVotado(self, ):
        pass

