from django.test import Client, TestCase
from django.urls import reverse_lazy

from flows.models import Fluxo


class PaginaInicialView(TestCase):
    def setUp(self):
        self.client = Client()
        self.targetUrl = reverse_lazy('flows:inicio')

    def test_get_tem_objeto_fluxos_em_contexto(self):
        """Get request retorna um objeto chamado fluxos em seu contexto"""
        response = self.client.get(self.targetUrl)
        self.assertIsNotNone(response.context.get('fluxos'))

    def test_get_com_banco_vazio(self):
        """Get request retorna lista de fluxos vazia quando não há objetos salvos"""
        response = self.client.get(self.targetUrl)
        fluxos = response.context.get('fluxos')
        self.assertEqual(0, len(fluxos))

    def test_get_com_banco_preenchido(self):
        """Get request retorna lista de fluxos não vazia quando há objetos salvos"""
        Fluxo.objects.create(nome="Fluxo 1")
        response = self.client.get(self.targetUrl)
        fluxos = response.context.get('fluxos')
        self.assertEqual(1, len(fluxos))
