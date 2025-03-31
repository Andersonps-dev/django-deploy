from django.test import TestCase
from django.urls import reverse
from deploy_app.models import Produto

class ProdutoListViewTest(TestCase):

    def setUp(self):
        """Cria produtos para testar a exibição da lista"""
        Produto.objects.create(nome="Camiseta", preco=59.90, estoque=100)
        Produto.objects.create(nome="Calça Jeans", preco=129.90, estoque=50)

    def test_lista_produtos(self):
        """Verifica se a página carrega e exibe os produtos"""
        response = self.client.get(reverse('listar_produtos'))  # Substituir pelo nome correto da URL no seu urls.py
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Camiseta")
        self.assertContains(response, "Calça Jeans")