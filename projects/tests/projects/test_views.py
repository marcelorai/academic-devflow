from django.test import TestCase
from django.urls import reverse_lazy
from projects.models import Projeto


class ProjetoUpdateView(TestCase):
    DESCRICAO = 'Teste do modelo projeto'
    DT_INICIO = '2010-10-10'
    DT_TERMINO = '2011-11-11'
    NOME = 'Teste'
    SITUACAO = 'Em desenvolvimento'

    PROJETO_OBJ = Projeto.objects.create(descricao=DESCRICAO, dt_inicio=DT_INICIO,
                                         dt_termino=DT_TERMINO, nome=NOME, situacao=SITUACAO)

    def test_edicao_do_projeto_solicitado(self):
        """Testa se o objeto retornado para edição é o solicitado"""

        url = reverse_lazy('projects:update', args=[self.PROJETO_OBJ.id])
        response = self.client.get(url)
        projeto_recebido = response.context['projeto']

        self.assertEqual(projeto_recebido.id, self.PROJETO_OBJ.id)

    def test_nome_do_projeto_editavel(self):
        """Testa se o campo 'nome' de um objeto Projeto é editável"""

        novo_nome = "nome 2"
        url = reverse_lazy('projects:update', args=[self.PROJETO_OBJ.id])
        data = {
            "descricao": self.PROJETO_OBJ.descricao,
            "dt_inicio": self.PROJETO_OBJ.dt_inicio,
            "dt_termino": self.PROJETO_OBJ.dt_termino,
            "nome": novo_nome,
            "situacao": self.PROJETO_OBJ.situacao
        }
        self.client.post(url, data)

        projeto_atualizado = Projeto.objects.filter(nome=novo_nome).first()
        self.assertIsNotNone(projeto_atualizado)
