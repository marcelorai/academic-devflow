from django.db import models

from .validators import validate_date_is_today_or_after


class Etapa(models.Model):
    numero = models.PositiveIntegerField(verbose_name='número')
    nome = models.CharField(max_length=100)
    descricao = models.TextField(
        max_length=400, verbose_name='descrição', blank=True, null=True)
    data_inicio = models.DateField(verbose_name='data de início')
    data_finalizacao = models.DateTimeField(
        verbose_name='data de finalização', validators=[validate_date_is_today_or_after])
    ativa = models.BooleanField(default=False)
    gameficada = models.BooleanField(default=False)
    # fluxo = foreign key para o fluxo a que a etapa pertence

    def __str__(self):
        return self.nome
