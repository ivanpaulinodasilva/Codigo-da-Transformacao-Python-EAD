import pytest
from app import app

@pytest.fixture
def client():
    """Simula o envio de requisições HTTP para a nossa API Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

# 1. Testando soma correta
def test_rota_somar_sucesso(client):
    resposta = client.post("/somar", json={"a": 10, "b": 20})
    dados = resposta.get_json()
    assert resposta.status_code == 200
    assert dados["resultado"] == 30

# 2. Testando divisão correta
def test_rota_dividir_sucesso(client):
    resposta = client.post("/dividir", json={"a": 10, "b": 2})
    dados = resposta.get_json()
    assert resposta.status_code == 200
    assert dados["resultado"] == 5

# 3. Testando erro de divisão por zero
def test_rota_dividir_por_zero(client):
    resposta = client.post("/dividir", json={"a": 10, "b": 0})
    dados = resposta.get_json()
    assert resposta.status_code == 400
    assert dados["erro"] == "Divisão por zero não é permitida."

# 4. Testando envio de dados inválidos (texto em vez de número)
def test_entrada_invalida(client):
    resposta = client.post("/somar", json={"a": "dez", "b": 5})
    dados = resposta.get_json()
    assert resposta.status_code == 400
    assert dados["erro"] == "Os valores devem ser números válidos."