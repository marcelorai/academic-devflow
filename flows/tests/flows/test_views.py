from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.utils import timezone

from flows.forms import AtualizarEtapaForm, CriarEtapaForm
from flows.models import Etapa, Fluxo


class EditarEtapaView(TestCase):
    def setUp(self):
        self.client = Client()
        self.fluxo_obj = Fluxo.objects.create(nome="Fluxo 2")
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
            'flows:editar_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': self.etapa_obj.id
            }
        )

    def test_get_tem_objeto_form_em_contexto(self):
        """Get request retorna um objeto chamado form em seu contexto"""
        response = self.client.get(self.targetUrl)
        self.assertIsNotNone(response.context.get('form'))

    def test_get_tem_objeto_form_do_tipo_AtualizarEtapaForm_em_contexto(self):
        """Get request retorna um objeto do tipo AtualizarEtapaForm em seu contexto"""
        response = self.client.get(self.targetUrl)
        form = response.context.get('form')
        self.assertIsInstance(form, AtualizarEtapaForm)

    def test_post_modificar_todos_os_campos_atualiza_objeto_etapa(self):
        """Post request com todos os campos atualiza um objeto do tipo Etapa"""
        data = {
            'nome': "Etapa 2",
            'descricao': "Uma velha etapa",
            'numero': '2',
            'data_inicio': '2022-12-02',
            'data_finalizacao': timezone.now().date(),
            'gameficada': False,
        }
        self.client.post(self.targetUrl, data)
        etapa_atualizada = Etapa.objects.get(id=self.etapa_obj.id)
        self.assertEqual(etapa_atualizada.nome, data.get('nome'))
        self.assertEqual(etapa_atualizada.descricao, data.get('descricao'))
        self.assertEqual(str(etapa_atualizada.numero), data.get('numero'))
        self.assertEqual(str(etapa_atualizada.data_inicio),
                         data.get('data_inicio'))
        self.assertEqual(etapa_atualizada.data_finalizacao,
                         data.get('data_finalizacao'))
        self.assertEqual(etapa_atualizada.gameficada, data.get('gameficada'))

    def test_post_de_dados_nao_cria_outro_objeto(self):
        """Post request com dados não criam um novo objeto"""
        data = {
            'nome': "Etapa 2",
            'descricao': "Uma velha etapa",
            'numero': '2',
            'data_inicio': '2022-12-02',
            'data_finalizacao': timezone.now().date(),
            'gameficada': False,
        }
        initial_count = Etapa.objects.count()
        self.client.post(self.targetUrl, data)
        current_count = Etapa.objects.count()
        self.assertEqual(current_count, initial_count)

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
        """Tentativa de acessar página de atualizacao de etapa em fluxo que não existe retorna erro 404"""
        targetUrl = reverse_lazy(
            'flows:editar_etapa',
            kwargs={
                'fluxo_pk': 100,
                'pk': self.etapa_obj.id
            }
        )
        response = self.client.get(targetUrl)
        self.assertEqual(response.status_code, 404)

    def test_get_com_etapa_inexistente_retorna_erro_404(self):
        """Tentativa de acessar página de atualização de etapa em etapa que não existe retorna erro 404"""
        targetUrl = reverse_lazy(
            'flows:editar_etapa',
            kwargs={
                'fluxo_pk': self.fluxo_obj.id,
                'pk': 25
            }
        )
        response = self.client.get(targetUrl)
        self.assertEqual(response.status_code, 404)
