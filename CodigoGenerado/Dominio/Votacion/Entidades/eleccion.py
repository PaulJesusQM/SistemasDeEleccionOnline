#-*- coding: utf-8 -*-

from django.db import models

class Eleccion(models.Model):
    class Meta:
        pass

    id = undefined()
    nombre = undefined()
    fecha_inicio = undefined()
    fecha_fin = undefined()
    resultado = undefined()


    def agregarCandidato(self, candidato):
        pass

    def calcularResultado(self, ):
        pass

    def obtenerElecciones(self, ):
        pass

    def registrarUsuario(self, usuario):
        pass

    def iniciarSesion(self, usuario, password):
        pass

