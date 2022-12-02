from django.test import Client, TestCase
from django.urls import reverse_lazy


class CreateArtifactView(TestCase):
    def setUp(self):
        self.client = Client()
        self.targetUrl = reverse_lazy('artifacts:registrar')
        self.testValues = {
            "nome": "Modelo de dados",
            "descricao": "Modelo de dados conceitual",
            "data_entrega": "2023-01-01",
            "situacao": "Em andamento"
        }

    def test_get_request_returns_form(self):
        """Verifica se a view exibe o formulário de criacao de artefato em request get"""

        response = self.client.get(self.targetUrl)
        self.assertIsNotNone(
            response.context, "Não foi usado contexto na renderização")
        self.assertIsNotNone(response.context.get('form'), "'form' não existe")
