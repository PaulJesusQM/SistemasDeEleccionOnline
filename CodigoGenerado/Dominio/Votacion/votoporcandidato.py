#-*- coding: utf-8 -*-

from django.db import models

class VotoPorCandidato(models.Model):
    class Meta:
        pass

    String candidatoId = None
    int cantidadVotos = None


