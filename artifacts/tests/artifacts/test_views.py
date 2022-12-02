from django.test import Client, TestCase
from django.urls import reverse_lazy
from artifacts.models import Artefato


class CreateArtifactView(TestCase):
    def setUp(self):
        self.client = Client()
        self.targetUrl = reverse_lazy('artifacts:registrar')
        self.test_values = {
            "nome": "Modelo de dados",
            "descricao": "Modelo de dados conceitual",
            "data_entrega": "2023-01-01",
            "situacao": "Em andamento"
        }

    def test_get_request_retorna_form(self):
        """Verifica se a view exibe o formulário de criacao de artefato em request get"""

        response = self.client.get(self.targetUrl)
        self.assertIsNotNone(
            response.context, "Não foi usado contexto na renderização")
        self.assertIsNotNone(response.context.get('form'), "'form' não existe")

    def test_post_request_todos_campos_cria_objeto(self):
        """Verifica se a view cria um Artefato quando todos os campos são passados em request post"""

        initial_count = Artefato.objects.count()
        self.client.post(self.targetUrl, self.test_values)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count+1)

    def test_post_request_campos_obrigatorios_cria_objeto(self):
        """Verifica se a view cria um Artefato quando os campos obrigatórios são passados em request post"""

        initial_count = Artefato.objects.count()
        request_data = {
            "nome": self.test_values['nome'],
            "data_entrega": self.test_values['data_entrega'],
            "situacao": self.test_values['situacao']
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count+1)

    def test_post_request_nome_ausente_nao_cria_objeto(self):
        """Verifica se a view não cria um Artefato quando o nome não é passado"""

        initial_count = Artefato.objects.count()
        request_data = {
            "data_entrega": self.test_values['data_entrega'],
            "situacao": self.test_values['situacao']
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count,
                         "Permite criar Artefato sem nome")

    def test_post_request_data_entrega_ausente_nao_cria_objeto(self):
        """Verifica se a view não cria um Artefato quando a data de entrega não é passada"""

        initial_count = Artefato.objects.count()
        request_data = {
            "nome": self.test_values['nome'],
            "situacao": self.test_values['situacao']
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count,
                         "Permite criar Artefato sem data de entrega")

    def test_post_request_situacao_ausente_nao_cria_objeto(self):
        """Verifica se a view não cria um Artefato quando a situação não é passada"""

        initial_count = Artefato.objects.count()
        request_data = {
            "nome": self.test_values['nome'],
            "data_entrega": self.test_values['data_entrega'],
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count,
                         "Permite criar Artefato sem situação")
