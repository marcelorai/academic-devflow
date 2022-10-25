from django.test import TestCase, Client
from projects.models import Projeto

from django.urls import reverse 

class TestViewNewProject(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('projects:register')
        self.ProjectTest = Projeto.objects.create(
            descricao = 'Descrição teste',
            dt_inicio = '2010-10-10',
            dt_termino = '2011-11-11',
            nome = 'Nome teste',
            situacao = 'Em desenvolvimento'
        )

    def test_view_new_project(self):
        url = self.register_url
        data = {
            "descricao": self.ProjectTest.descricao,
            "dt_inicio": self.ProjectTest.dt_inicio,
            "dt_termino": self.ProjectTest.dt_termino,
            "nome": self.ProjectTest.nome,
            "situacao": self.ProjectTest.situacao
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.ProjectTest.nome, 'Nome teste')

