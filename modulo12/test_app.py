import pytest
from app import app

@pytest.fixture
def client():
    """Fixture do pytest para simular requisições HTTP na API Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# Teste da rota /somar com entradas válidas
def test_rota_somar_sucesso(client):
    resposta = client.post("/somar", json={"a": 10, "b": 20})
    dados = resposta.get_json()
    
    assert resposta.status_code == 200
    assert dados["resultado"] == 30

# Teste da rota /dividir com entradas válidas
def test_rota_dividir_sucesso(client):
    resposta = client.post("/dividir", json={"a": 10, "b": 2})
    dados = resposta.get_json()
    
    assert resposta.status_code == 200
    assert dados["resultado"] == 5

# Teste de validação: divisão por zero na API
def test_rota_dividir_por_zero(client):
    resposta = client.post("/dividir", json={"a": 10, "b": 0})
    dados = resposta.get_json()
    
    assert resposta.status_code == 400
    assert dados["erro"] == "Divisão por zero não é permitida."

# Teste de validação: entrada de tipo inválido
def test_entrada_invalida(client):
    resposta = client.post("/somar", json={"a": "dez", "b": 5})
    dados = resposta.get_json()
    
    assert resposta.status_code == 400
    assert dados["erro"] == "Os valores devem ser números válidos."