import unittest
from app import app  # Importa a sua aplicação Flask

class TesteAPIFlask(unittest.TestCase):

    def setUp(self):
        """Configura o cliente de testes do Flask antes de cada teste."""
        app.config["TESTING"] = True
        self.client = app.test_client()

    # Teste da rota /somar com sucesso
    def test_rota_somar_sucesso(self):
        resposta = self.client.post("/somar", json={"a": 10, "b": 20})
        dados = resposta.get_json()
        
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(dados["resultado"], 30)

    # Teste da rota /dividir com sucesso
    def test_rota_dividir_sucesso(self):
        resposta = self.client.post("/dividir", json={"a": 10, "b": 2})
        dados = resposta.get_json()
        
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(dados["resultado"], 5)

    # Teste de validação: Divisão por zero
    def test_rota_dividir_por_zero(self):
        resposta = self.client.post("/dividir", json={"a": 10, "b": 0})
        dados = resposta.get_json()
        
        self.assertEqual(resposta.status_code, 400)
        self.assertEqual(dados["erro"], "Divisão por zero não é permitida.")

    # Teste de validação: Entrada inválida
    def test_entrada_invalida(self):
        resposta = self.client.post("/somar", json={"a": "dez", "b": 5})
        dados = resposta.get_json()
        
        self.assertEqual(resposta.status_code, 400)
        self.assertEqual(dados["erro"], "Os valores devem ser números válidos.")

if __name__ == "__main__":
    unittest.main()