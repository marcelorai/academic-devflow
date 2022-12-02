from django.test import TestCase
from artifacts.models import Artefato


class ArtefatoModel(TestCase):
    DESCRICAO = "Modelo de dados conceitual"
    NOME = "Modelo de dados"
    SITUACAO = "Entregue"
    DATA_ENTREGA = '2022-12-12'

    def test_objeto_criado_todos_campos(self):
        """O modelo cria corretamente o objeto quando todos os atributos são fornecidos"""

        a = Artefato.objects.create(descricao=self.DESCRICAO, nome=self.NOME,
                                    situacao=self.SITUACAO, data_entrega=self.DATA_ENTREGA)
        self.assertTrue(isinstance(a, Artefato))
        self.assertEqual(a.nome, self.NOME)

    def test_objeto_criado_campos_obrigatorios(self):
        """O modelo cria corretamente o objeto quando apenas os atributos obrigatórios são fornecidos"""

        a = Artefato.objects.create(nome=self.NOME, situacao=self.SITUACAO,
                                    data_entrega=self.DATA_ENTREGA)
        self.assertTrue(isinstance(a, Artefato))
        self.assertEqual(a.nome, self.NOME)
