from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.utils import timezone

from flows.models import Etapa, Fluxo


class ExcluirEtapaView(TestCase):
    def setUp(self):
        self.client = Client()
        self.fluxo_obj = Fluxo.objects.create(nome="Fluxo 1")
        self.etapa_obj = Etapa.objects.create(
            nome="Etapa 1",
            descricao="Uma nova etapa",
            numero='1',
            data_inicio='2022-12-01',
            data_finalizacao=timezone.now().date(),
            gameficada=True,
            fluxo=self.fluxo_obj
        )
        self.targetUrl = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': self.etapa_obj.id
            }
        )

    def test_post_apaga_etapa(self):
        "Post request remove etapa de fluxo"
        initial_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.client.post(self.targetUrl)
        current_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.assertEqual(initial_count-1, current_count)

    def test_get_nao_apaga_etapa(self):
        "Get request não remove etapa de fluxo"
        initial_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.client.get(self.targetUrl)
        current_count = Fluxo.objects.get(
            id=self.fluxo_obj.id).etapa_set.count()
        self.assertEqual(initial_count, current_count)

    def test_post_redireciona_para_detalhes_fluxo(self):
        """Após a realização de um post request a view redireciona a página de detalhes do fluxo"""
        expected_url = reverse_lazy('flows:detalhes_fluxo', kwargs={
                                    'pk': self.fluxo_obj.id})
        response = self.client.post(self.targetUrl)
        self.assertRedirects(response, expected_url)

    def test_get_com_fluxo_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página (get) com fluxo que não existe retorna erro 404"""
        targetUrl = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': 100,
                'pk': self.etapa_obj.id
            }
        )
        response = self.client.get(targetUrl)
        self.assertEqual(response.status_code, 404)

    def test_get_com_etapa_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página (get) com etapa que não existe retorna erro 404"""
        targetUrl = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': 25
            }
        )
        response = self.client.get(targetUrl)
        self.assertEqual(response.status_code, 404)

    def test_post_com_fluxo_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página (post) com fluxo que não existe retorna erro 404"""
        targetUrl = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': 100,
                'pk': self.etapa_obj.id
            }
        )
        response = self.client.get(targetUrl)
        self.assertEqual(response.status_code, 404)

    def test_post_com_etapa_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página (post) com etapa que não existe retorna erro 404"""
        targetUrl = reverse_lazy(
            'flows:excluir_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': 25
            }
        )
        response = self.client.get(targetUrl)
        self.assertEqual(response.status_code, 404)
