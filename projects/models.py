from django.db import models


class Projeto(models.Model):
    descricao = models.TextField(blank=True, null=True)
    dt_inicio = models.DateField()
    dt_termino = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=70)
    situacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
