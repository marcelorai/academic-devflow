from datetime import timedelta

from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.utils import timezone

from flows.models import Etapa, Fluxo


class ExcluirEtapaView(TestCase):
    def setUp(self):
        self.client = Client()
        self.fluxo_obj = Fluxo.objects.create(nome="Fluxo 1")
        self.etapa_iniciada = Etapa.objects.create(
            nome="Etapa 1",
            descricao="Uma nova etapa",
            numero='1',
            data_inicio='2022-12-01',
            data_finalizacao=timezone.now().date(),
            gameficada=True,
            fluxo=self.fluxo_obj
        )
        self.etapa_nao_iniciada = Etapa.objects.create(
            nome="Etapa 2",
            descricao="Uma nova etapa",
            numero='2',
            data_inicio=(timezone.now() + timedelta(days=1)).date(),
            data_finalizacao=(timezone.now() + timedelta(days=10)).date(),
            gameficada=True,
            fluxo=self.fluxo_obj
        )
        self.target_url_etapa_iniciada = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': self.etapa_iniciada.id
            }
        )
        self.target_url_etapa_nao_iniciada = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': self.etapa_nao_iniciada.id
            }
        )

    def test_post_etapa_nao_iniciada_apaga_etapa(self):
        "Post request remove etapa de fluxo quando ela não iniciou ainda"
        initial_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.client.post(self.target_url_etapa_nao_iniciada)
        current_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.assertEqual(initial_count-1, current_count)

    def test_post_etapa_iniciada_nao_apaga_etapa(self):
        "Post request não remove etapa de fluxo quando ela já iniciou"
        initial_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.client.post(self.target_url_etapa_iniciada)
        current_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.assertEqual(initial_count, current_count)

    def test_get_nao_apaga_etapa_iniciada(self):
        "Get request não remove etapa de fluxo quando ela já iniciou"
        initial_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.client.get(self.target_url_etapa_iniciada)
        current_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.assertEqual(initial_count, current_count)

    def test_get_nao_apaga_etapa_nao_iniciada(self):
        "Get request não remove etapa de fluxo quando ela não iniciou"
        initial_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.client.get(self.target_url_etapa_nao_iniciada)
        current_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.assertEqual(initial_count, current_count)

    def test_post_redireciona_para_detalhes_fluxo(self):
        """Após um post request de sucesso a view redireciona a página de detalhes do fluxo"""
        expected_url = reverse_lazy('flows:detalhes_fluxo', kwargs={
                                    'pk': self.fluxo_obj.id})
        response = self.client.post(self.target_url_etapa_nao_iniciada)
        self.assertRedirects(response, expected_url)

    def test_get_com_fluxo_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página (get) com fluxo que não existe retorna erro 404"""
        target_url = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': 100,
                'pk': self.etapa_nao_iniciada.id
            }
        )
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 404)

    def test_get_com_etapa_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página (get) com etapa que não existe retorna erro 404"""
        target_url = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': 25
            }
        )
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 404)

    def test_post_com_fluxo_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página (post) com fluxo que não existe retorna erro 404"""
        target_url = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': 100,
                'pk': self.etapa_nao_iniciada.id
            }
        )
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 404)

    def test_post_com_etapa_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página (post) com etapa que não existe retorna erro 404"""
        target_url = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': 25
            }
        )
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 404)
