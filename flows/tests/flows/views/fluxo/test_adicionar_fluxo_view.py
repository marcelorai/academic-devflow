from django.test import Client, TestCase
from django.urls import reverse_lazy

from flows.forms import CriarFluxoForm
from flows.models import Fluxo


class AdicionarFluxoView(TestCase):
    def setUp(self):
        self.client = Client()
        self.targetUrl = reverse_lazy('flows:adicionar_fluxo')

    def test_get_tem_objeto_form_em_contexto(self):
        """Get request retorna um objeto chamado form em seu contexto"""
        response = self.client.get(self.targetUrl)
        self.assertIsNotNone(response.context.get('form'))

    def test_get_tem_objeto_form_do_tipo_CriarFluxoForm_em_contexto(self):
        """Get request retorna um objeto do tipo CriarFluxoForm em seu contexto"""
        response = self.client.get(self.targetUrl)
        form = response.context.get('form')
        self.assertIsInstance(form, CriarFluxoForm)

    def test_post_todos_os_campos_cria_objeto_fluxo(self):
        """Post request com todos os campos cria um objeto do tipo Fluxo"""
        data = {
            'nome': "Fluxo 1",
            'descricao': "Um novo fluxo"
        }
        initial_count = Fluxo.objects.count()
        self.client.post(self.targetUrl, data)
        current_count = Fluxo.objects.count()
        self.assertEqual(current_count, initial_count+1)

    def test_post_campos_obrigatorios_cria_objeto_fluxo(self):
        """Post request com os campos obrigatórios cria um objeto do tipo Fluxo"""
        data = {
            'nome': "Fluxo 2"
        }
        initial_count = Fluxo.objects.count()
        self.client.post(self.targetUrl, data)
        current_count = Fluxo.objects.count()
        self.assertEqual(current_count, initial_count+1)

    def test_post_de_dados_incompletos_nao_cria_objeto_fluxo(self):
        """Post request com campos incompletos não cria um objeto do tipo Fluxo"""
        data = {
            'descricao': "Um novo fluxo"
        }
        initial_count = Fluxo.objects.count()
        self.client.post(self.targetUrl, data)
        current_count = Fluxo.objects.count()
        self.assertEqual(current_count, initial_count)

    def test_post_redireciona_para_pagina_inicial(self):
        """Após a realização de um post request de sucesso a view redireciona a página inicial de fluxos"""
        data = {
            'nome': "Fluxo 3"
        }
        response = self.client.post(self.targetUrl, data)
        self.assertRedirects(response, reverse_lazy('flows:inicio'))
