import os

# 1. Mapeando a pasta meus_arquivos dentro do modulo06
pasta_modulo06 = os.path.dirname(os.path.abspath(__file__))
pasta_meus_arquivos = os.path.join(pasta_modulo06, "meus_arquivos")

# Garante que a pasta meus_arquivos exista dentro do modulo06
if not os.path.exists(pasta_meus_arquivos):
    os.makedirs(pasta_meus_arquivos)

caminho_arquivo = os.path.join(pasta_meus_arquivos, "dados_arquivo.txt")

# 2. Conteúdo a ser escrito
conteudo = [
    "Ivan Silva;40 anos;02899-000;947541;ivanpaulino@mail.com\n",
    "Beatriz Vitoria;30 anos;057193-000;978786;beavitoria@mail.com\n",
    "Eric Renan;17 anos;089880-100;98799;ericrenan@gmail.com\n",
]

# 3. Escrita no arquivo TXT
with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(conteudo)

print("✓ Arquivo 'dados_arquivo.txt' salvo em: modulo06/meus_arquivos/\n")

# 4. Leitura e exibição
print("--- Lendo o conteúdo do arquivo TXT ---")
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    print(arquivo.read())