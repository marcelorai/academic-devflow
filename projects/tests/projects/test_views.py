from urllib import response
from django.test import TestCase, Client
from projects.models import Projeto

from django.urls import reverse 

class TestViewPostProject(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.ProjectTest = Projeto.objects.create(
            descricao = 'Descrição teste',
            dt_inicio = '2010-10-10',
            dt_termino = '2011-11-11',
            nome = 'Nome teste',
            situacao = 'Em desenvolvimento'
        )

    def test_view_post_project(self):

        response = self.client.post(self.register_url, {
            self.ProjectTest
        })

        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.ProjectTest.nome, 'Nome Teste')

