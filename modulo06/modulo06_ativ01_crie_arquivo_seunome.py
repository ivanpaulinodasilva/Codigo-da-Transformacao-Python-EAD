'''




'''
# 1 . Criando um arquivo TXT com o nome "nome_arquivo.txt" 
# e escrevendo algumas informações nele.
nome_arquivo = "dados_arquivo.txt"


# 2 . Conteúdo a ser escrito no arquivo
# --- ESCRITA ---
conteudo = [
    "Ivan Silva;40 anos;02899-000;947541;ivanpaulino@mail.com\n",
    "Beatriz Vitoria;30 anos;057193-000;978786;beavitoria@mail.com\n",
    "Eric Renan;17 anos;089880-100;98799;ericrenan@gmail.com\n"
]


# 3 . Escrevendo no arquivo
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.writelines(conteudo)
print(f"✅ Arquivo '{nome_arquivo}' criado e escrito com sucesso!")



# 4 . Lendo o conteúdo do arquivo
# --- LEITURA ---
print("\n--- Lendo o conteúdo do arquivo TXT ---")
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    print(texto)