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
            "data-entrega": "2023-01-01",
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
            "data-entrega": self.test_values['data-entrega'],
            "situacao": self.test_values['situacao']
        }
        self.client.post(self.targetUrl, request_data)
        current_count = Artefato.objects.count()
        self.assertEqual(current_count, initial_count+1)
