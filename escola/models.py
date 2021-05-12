from django.db import models
from django.db.models import Model


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)

    def __str__(self):
        return self.nome