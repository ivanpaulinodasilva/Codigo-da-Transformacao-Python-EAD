import json

nome_arquivo = "clientes_nomes.json"

# Dicionário/Lista com os dados dos clientes
clientes = [
    {
        "Nome completo": "Ivan Silva",
        "idade": "40 anos",
        "CEP": "02899-000",
        "ResgMatr": "947541",
        "E-Mail": "ivanpaulino@mail.com"
    },
    {
        "Nome completo": "Beatriz Vitoria",
        "idade": "30 anos",
        "CEP": "057193-000",
        "ResgMatr": "978786",
        "E-Mail": "beavitoria@mail.com"
    },
    {
        "Nome completo": "Eric Renan",
        "idade": "17 anos",
        "CEP": "089880-100",
        "ResgMatr": "98799",
        "E-Mail": "ericrenan@gmail.com"
    }
]

# --- ESCRITA (Salvar) ---
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, ensure_ascii=False, indent=2)
print(f"✅ Dados salvos em '{nome_arquivo}' com sucesso!")

# --- LEITURA (Carregar) ---
print("\n--- Carregando dados do arquivo JSON ---")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    clientes_carregados = json.load(arquivo)

for cliente in clientes_carregados:
    print(f"Cliente: {cliente['Nome completo']} | E-Mail: {cliente['E-Mail']}")