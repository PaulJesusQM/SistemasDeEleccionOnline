#-*- coding: utf-8 -*-

from django.db import models

from Dominio.Usuario.Entidades.Elector import Elector

class Voto(Elector):
    class Meta:
        pass

    id = undefined()
    elector = undefined()
    candidato = undefined()
    fecha = undefined()


    def getId(self, ):
        pass

    def getEleccion(self, ):
        pass

    def getCandidato(self, ):
        pass

    def getElector(self, ):
        pass

    def Operation1(self, ):
        pass

