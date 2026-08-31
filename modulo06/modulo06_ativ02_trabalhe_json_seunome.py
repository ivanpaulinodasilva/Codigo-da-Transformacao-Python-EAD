import json
import os

# 1. Mapeando a pasta meus_arquivos dentro do modulo06
pasta_modulo06 = os.path.dirname(os.path.abspath(__file__))
pasta_meus_arquivos = os.path.join(pasta_modulo06, "meus_arquivos")

if not os.path.exists(pasta_meus_arquivos):
    os.makedirs(pasta_meus_arquivos)

caminho_arquivo = os.path.join(pasta_meus_arquivos, "clientes_nomes.json")

# 2. Estrutura de dados dos clientes
clientes = [
    {
        "Nome completo": "Ivan Silva",
        "Idade": "40 anos",
        "CEP": "02899-000",
        "ResgMatr": "947541",
        "E-Mail": "ivanpaulino@mail.com",
    },
    {
        "Nome completo": "Beatriz Vitoria",
        "Idade": "30 anos",
        "CEP": "057193-000",
        "ResgMatr": "978786",
        "E-Mail": "beavitoria@mail.com",
    },
    {
        "Nome completo": "Eric Renan",
        "Idade": "17 anos",
        "CEP": "089880-100",
        "ResgMatr": "98799",
        "E-Mail": "ericrenan@gmail.com",
    },
]

# 3. Escrita no arquivo JSON
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, ensure_ascii=False, indent=2)

print("✓ Arquivo 'clientes_nomes.json' salvo em: modulo06/meus_arquivos/\n")

# 4. Leitura do arquivo JSON
print("--- Carregando dados do arquivo JSON ---")
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    clientes_carregados = json.load(arquivo)

for cliente in clientes_carregados:
    print(f"Cliente: {cliente['Nome completo']} | E-Mail: {cliente['E-Mail']}")