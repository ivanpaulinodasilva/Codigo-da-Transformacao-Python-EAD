'''
==============================================================================
 AULA PRÁTICA: CONSUMO DE API E PAIR PROGRAMMING (PYTHON)
==============================================================================
 Pré-requisito no terminal:
 pip install requests

 👥 DIVISÃO DOS PAPÉIS E REGRAS (Pair Programming):
 🧑‍💻 Driver (Piloto): 
    - Fica no teclado[cite: 1, 2].
    - Escreve a sintaxe Python, declara as variáveis em snake_case e executa o código[cite: 1, 2].
 
 🧭 Navigator (Navegador): 
    - Não toca no teclado[cite: 1, 2].
    - Analisa a estrutura do JSON, orienta a lógica e confere se as variáveis usam snake_case[cite: 1, 2].
 
 ⏱️ Timer: 
    - Troca obrigatória de papéis a cada 15-20 minutos[cite: 1, 2].
==============================================================================
'''

import requests

def consultar_clima():
    # ------------------------------------------------------------------------
    # BLOCO 1: ENTRADA DE DADOS E CONFIGURAÇÕES DA API (Foco do Par 1)[cite: 1, 2]
    # ------------------------------------------------------------------------
    # 1. Entrada do nome da cidade pelo usuário
    cidade = input("Digite o nome da cidade: ").strip()
    
    # 2. Chave de acesso individual da OpenWeatherMap
    chave_api = "2d6690b51aa4015324c330bb1bfa1a7f" 
    
    # --- PASSO A: Buscar Estado e Coordenadas via Geocoding API ---
    url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={cidade}&limit=1&appid={chave_api}"
    resposta_geo = requests.get(url_geo)
    
    estado = ""
    pais = ""
    
    # Validação da busca de geolocalização
    if resposta_geo.status_code == 200 and len(resposta_geo.json()) > 0:
        dados_geo = resposta_geo.json()[0]
        # Captura as chaves 'state' e 'country' do JSON
        estado = dados_geo.get("state", "")
        pais = dados_geo.get("country", "")

    # ------------------------------------------------------------------------
    # 🔄 RECOMENDAÇÃO DE TROCA DE PAPÉIS (Driver ↔ Navigator)[cite: 1, 2]
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # BLOCO 2: REQUISIÇÃO HTTP E EXTRAÇÃO DE DADOS (Foco do Par 2)[cite: 1, 2]
    # ------------------------------------------------------------------------
    # URL formatada para consulta de clima atual (unidades em Celsius e texto em Português)
    url_api = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"

    print("\nBuscando dados com OpenWeatherMap...")
    
    # 3. Requisição HTTP GET[cite: 1]
    resposta = requests.get(url_api)

    # 4. Tratamento do retorno e validação do Status Code[cite: 1]
    if resposta.status_code == 200:
        dados_clima = resposta.json()

        # Extração de informações do dicionário aninhado (JSON) em variáveis snake_case[cite: 1]
        nome_cidade = dados_clima["name"]
        temperatura = dados_clima["main"]["temp"]
        sensacao_termica = dados_clima["main"]["feels_like"]
        descricao_clima = dados_clima["weather"][0]["description"]
        umidade = dados_clima["main"]["humidity"]

        # Formatação dinâmica da localização
        if estado:
            localizacao = f"{nome_cidade} - {estado}, {pais}"
        else:
            localizacao = f"{nome_cidade}, {pais}"

        # Exibição formatada dos resultados
        print("\n" + "=" * 40)
        print(f"🌍 Clima atual em: {localizacao}")
        print("=" * 40)
        print(f"🌤️  Condição: {descricao_clima.capitalize()}")
        print(f"🌡️  Temperatura: {temperatura}°C")
        print(f"🔥 Sensação Térmica: {sensacao_termica}°C")
        print(f"💧 Umidade: {umidade}%")
        print("=" * 40)

    # ------------------------------------------------------------------------
    # TRATAMENTO DE ERROS DE CONEXÃO E REQUISIÇÃO HTTP[cite: 1]
    # ------------------------------------------------------------------------
    elif resposta.status_code == 401:
        print("\n❌ Erro 401: Chave de API não autorizada.")
        print("Verifique se inseriu a chave correta ou se aguardou a ativação do OpenWeatherMap.")

    elif resposta.status_code == 404:
        print(f"\n❌ Erro 404: Cidade '{cidade}' não encontrada.")
        print("Verifique a grafia do nome da cidade e tente novamente.")

    else:
        print(f"\n⚠️ Falha na requisição. Código de erro HTTP: {resposta.status_code}")

# Execução principal
if __name__ == "__main__":
    consultar_clima()