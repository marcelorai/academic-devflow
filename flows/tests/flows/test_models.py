from django.test import TestCase
from flows.models import Etapa, Fluxo
from django.utils import timezone


class EtapaModel(TestCase):
    def setUp(self):
        self.fluxo = Fluxo.objects.create(nome="XP")
        self.nome = 'Planejamento'
        self.descricao = 'Pensando o funcionamento do projeto'
        self.data_inicio = timezone.now()
        self.data_finalizacao = timezone.now()
        self.gameficada = False
        self.numero = 1
        self.ativa = True

    def test_objeto_criado_todos_campos(self):
        """O modelo cria corretamente o objeto quando todos os atributos são fornecidos"""
        etapa = Etapa.objects.create(numero=self.numero, nome=self.nome, descricao=self.descricao, data_inicio=self.data_inicio,
                                     data_finalizacao=self.data_finalizacao, ativa=self.ativa, gameficada=self.gameficada, fluxo=self.fluxo)
        self.assertIsInstance(etapa, Etapa)
        self.assertEqual(self.nome, etapa.nome)

    def test_objeto_criado_campos_obrigatorios(self):
        """O modelo cria corretamente o objeto quando apenas os atributos obrigatórios são fornecidos"""
        etapa = Etapa.objects.create(numero=self.numero, nome=self.nome, data_inicio=self.data_inicio,
                                     data_finalizacao=self.data_finalizacao, ativa=self.ativa, gameficada=self.gameficada, fluxo=self.fluxo)
        self.assertIsInstance(etapa, Etapa)
        self.assertEqual(self.nome, etapa.nome)
