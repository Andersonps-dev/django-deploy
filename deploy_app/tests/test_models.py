from django.test import TestCase
from deploy_app.models import Produto

class ProdutoModelTest(TestCase):

    def setUp(self):
        """Configura os dados iniciais para os testes"""
        self.produto = Produto.objects.create(
            nome="Camiseta",
            preco=59.90,
            estoque=100
        )

    def test_criacao_produto(self):
        """Verifica se o produto foi criado corretamente"""
        produto = Produto.objects.get(nome="Camiseta")
        self.assertEqual(produto.preco, 59.90)
        self.assertEqual(produto.estoque, 100)