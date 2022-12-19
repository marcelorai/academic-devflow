from django.test import Client, TestCase
from django.urls import reverse_lazy

from flows.models import Fluxo


class DetalhesFluxoView(TestCase):
    def setUp(self):
        self.client = Client()
        self.fluxo_obj = Fluxo.objects.create(nome='Fluxo 1')

    def test_get_tem_objeto_fluxo_em_contexto(self):
        """Get request retorna um objeto chamado fluxo em seu contexto"""
        targetUrl = reverse_lazy('flows:detalhes_fluxo', kwargs={
                                 'pk': self.fluxo_obj.id})
        response = self.client.get(targetUrl)
        self.assertIsNotNone(response.context.get('fluxo'))

    def test_get_retorna_objeto_desejado(self):
        """Get request retorna um objeto chamado fluxo em seu contexto"""
        targetUrl = reverse_lazy('flows:detalhes_fluxo', kwargs={
                                 'pk': self.fluxo_obj.id})
        response = self.client.get(targetUrl)
        fluxo_retornado = response.context.get('fluxo')
        self.assertEqual(self.fluxo_obj.nome, fluxo_retornado.nome)

    def test_get_com_pk_inexistente_retorna_erro_404(self):
        """Get request retorna erro 404 quando nao há fluxo com a primary key passada"""
        targetUrl = reverse_lazy('flows:detalhes_fluxo', kwargs={
                                 'pk': 100})
        response = self.client.get(targetUrl)
        self.assertEqual(response.status_code, 404)
