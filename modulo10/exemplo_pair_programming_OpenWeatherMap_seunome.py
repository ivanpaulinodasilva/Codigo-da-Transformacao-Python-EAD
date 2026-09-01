import requests

def consultar_clima():
    # 1. Entrada de dados
    cidade = input("Digite o nome da cidade: ").strip()
    
    # 2. Configurações da API
    chave_api = "2d6690b51aa4015324c330bb1bfa1a7f" 
    
    # --- PASSO A: Buscar Estado e Coordenadas (Geocoding API) ---
    url_geo = f"http://api.openweathermap.org/geo/1.0/direct?q={cidade}&limit=1&appid={chave_api}"
    resposta_geo = requests.get(url_geo)
    
    estado = ""
    pais = ""
    
    if resposta_geo.status_code == 200 and len(resposta_geo.json()) > 0:
        dados_geo = resposta_geo.json()[0]
        # Captura o Estado e País retornados pela Geocoding API
        estado = dados_geo.get("state", "")
        pais = dados_geo.get("country", "")

    # --- PASSO B: Buscar Clima Atual ---
    url_api = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"

    print("\nBuscando dados com OpenWeatherMap...")
    
    # 3. Requisição HTTP GET
    resposta = requests.get(url_api)

    # 4. Tratamento do retorno e validação do Status Code
    if resposta.status_code == 200:
        dados_clima = resposta.json()

        # Extração de informações do dicionário aninhado
        nome_cidade = dados_clima["name"]
        temperatura = dados_clima["main"]["temp"]
        sensacao_termica = dados_clima["main"]["feels_like"]
        descricao_clima = dados_clima["weather"][0]["description"]
        umidade = dados_clima["main"]["humidity"]

        # Formatação do local (Cidade - Estado, País)
        if estado:
            localizacao = f"{nome_cidade} - {estado}, {pais}"
        else:
            localizacao = f"{nome_cidade}, {pais}"

        # Exibição dos dados organizados
        print("\n" + "=" * 40)
        print(f"🌍 Clima atual em: {localizacao}")
        print("=" * 40)
        print(f"🌤️  Condição: {descricao_clima.capitalize()}")
        print(f"🌡️  Temperatura: {temperatura}°C")
        print(f"🔥 Sensação Térmica: {sensacao_termica}°C")
        print(f"💧 Umidade: {umidade}%")
        print("=" * 40)

    elif resposta.status_code == 401:
        print("\n❌ Erro 401: Chave de API não autorizada.")
        print("Verifique se inseriu a chave correta ou se aguardou a ativação do OpenWeatherMap.")

    elif resposta.status_code == 404:
        print(f"\n❌ Erro 404: Cidade '{cidade}' não encontrada.")
        print("Verifique a grafia do nome da cidade e tente novamente.")

    else:
        print(f"\n⚠️ Falha na requisição. Código de erro HTTP: {resposta.status_code}")

# Execução do programa
if __name__ == "__main__":
    consultar_clima()