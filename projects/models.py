from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=70)
    descricao = models.TextField(blank=True, null=True)
    data_inicio = models.DateField()
    data_termino = models.DateField(blank=True, null=True)
    situacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

