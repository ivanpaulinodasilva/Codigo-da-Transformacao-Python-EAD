from django.test import TestCase
from django.urls import reverse
from modulo14.models import Produto

class ProdutoModelTest(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Teclado Mecânico",
            descricao="Teclado RGB switch azul",
            preco=250.00,
            quantidade=10
        )

    def test_produto_creation(self):
        self.assertEqual(self.produto.nome, "Teclado Mecânico")
        self.assertEqual(float(self.produto.preco), 250.00)
        self.assertEqual(str(self.produto), "Teclado Mecânico")

class ProdutoViewsTest(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Mouse Gamer",
            descricao="Mouse 10000 DPI",
            preco=120.00,
            quantidade=5
        )

    def test_produto_list_view(self):
        response = self.client.get(reverse('produto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mouse Gamer")

    def test_produto_create_view(self):
        response = self.client.post(reverse('produto_create'), {
            'nome': 'Monitor',
            'descricao': 'Monitor 144Hz',
            'preco': 1200.00,
            'quantidade': 3
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Produto.objects.count(), 2)

    def test_produto_update_view(self):
        response = self.client.post(reverse('produto_update', args=[self.produto.pk]), {
            'nome': 'Mouse Gamer Sem Fio',
            'descricao': 'Mouse 10000 DPI',
            'preco': 150.00,
            'quantidade': 5
        })
        self.assertEqual(response.status_code, 302)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, 'Mouse Gamer Sem Fio')

    def test_produto_delete_view(self):
        response = self.client.post(reverse('produto_delete', args=[self.produto.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Produto.objects.count(), 0)