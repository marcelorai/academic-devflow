from django.test import Client, TestCase
from django.urls import reverse_lazy

from flows.forms import CriarFluxoForm, CriarEtapaForm
from flows.models import Fluxo, Etapa
from django.utils import timezone


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

    def test_post_redireciona_para_pagina_inicial(self):
        """Após a realização de um post request de sucesso a view redireciona a página inicial de fluxos"""
        data = {
            'nome': "Fluxo 3"
        }
        response = self.client.post(self.targetUrl, data)
        self.assertRedirects(response, reverse_lazy('flows:inicio'))


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


class AdicionarEtapaView(TestCase):
    def setUp(self):
        self.client = Client()
        self.fluxo_obj = Fluxo.objects.create(nome="Fluxo 2")
        self.targetUrl = reverse_lazy('flows:adicionar_etapa', kwargs={
                                      'fluxo_pk': self.fluxo_obj.id})

    def test_get_tem_objeto_form_em_contexto(self):
        """Get request retorna um objeto chamado form em seu contexto"""
        response = self.client.get(self.targetUrl)
        self.assertIsNotNone(response.context.get('form'))

    def test_get_tem_objeto_form_do_tipo_CriarEtapaForm_em_contexto(self):
        """Get request retorna um objeto do tipo CriarEtapaForm em seu contexto"""
        response = self.client.get(self.targetUrl)
        form = response.context.get('form')
        self.assertIsInstance(form, CriarEtapaForm)

    def test_post_todos_os_campos_cria_objeto_etapa(self):
        """Post request com todos os campos cria um objeto do tipo Etapa"""
        data = {
            'nome': "Etapa 1",
            'descricao': "Uma nova etapa",
            'numero': '1',
            'data_inicio': '2022-12-01',
            'data_finalizacao': timezone.now().date(),
            'gameficada': True,
        }
        initial_count = Etapa.objects.count()
        self.client.post(self.targetUrl, data)
        current_count = Etapa.objects.count()
        self.assertEqual(current_count, initial_count+1)

    def test_post_campos_obrigatorios_cria_objeto_etapa(self):
        """Post request com os campos obrigatórios cria um objeto do tipo Etpa"""
        data = {
            'nome': "Etapa 1",
            'numero': '1',
            'data_inicio': '2022-12-01',
            'data_finalizacao': timezone.now().date(),
            'gameficada': True,
        }
        initial_count = Etapa.objects.count()
        self.client.post(self.targetUrl, data)
        current_count = Etapa.objects.count()
        self.assertEqual(current_count, initial_count+1)

    def test_post_redireciona_para_detalhes_fluxo(self):
        """Após a realização de um post request de sucesso a view redireciona a página de detalhes do fluxo"""
        data = {
            'nome': "Etapa 1",
            'descricao': "Uma nova etapa",
            'numero': '1',
            'data_inicio': '2022-12-01',
            'data_finalizacao': timezone.now().date(),
            'gameficada': True,
        }
        response = self.client.post(self.targetUrl, data)
        expected_url = reverse_lazy('flows:detalhes_fluxo', kwargs={
                                    'pk': self.fluxo_obj.id})
        self.assertRedirects(response, expected_url)

    def test_get_com_fluxo_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página de cadastro de etapa em fluxo que não existe retorna erro 404"""
        targetUrl = reverse_lazy('flows:adicionar_etapa', kwargs={
                                 'fluxo_pk': 100})
        response = self.client.get(targetUrl)
        self.assertEqual(response.status_code, 404)

    def test_dados_incompletos_nao_cria_objeto(self):
        """Post request com apenas parte dos dados não cria objeto"""
        initial_count = Etapa.objects.count()
        data = {
            'nome': "Etapa 1",
        }
        self.client.post(self.targetUrl, data)
        current_count = Etapa.objects.count()
        self.assertEqual(initial_count, current_count)
