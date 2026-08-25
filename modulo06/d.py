# 4_desafio_backup_shutil.py
import shutil
import os

def realizar_backup(pasta_origem, pasta_destino):
    # Verifica se a pasta de origem existe
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não existe.")
        return

    # Garante que a pasta de destino seja criada, caso não exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Diretório de destino '{pasta_destino}' criado.")

    # Listar e copiar todos os arquivos do diretório de origem
    arquivos = os.listdir(pasta_origem)
    for arquivo in arquivos:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        
        # Copia apenas arquivos (ignora subdiretórios neste exemplo simples)
        if os.path.isfile(caminho_origem):
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"Copiado: {arquivo} -> {pasta_destino}")

    print("\nBackup concluído com sucesso!")

if __name__ == "__main__":
    # Exemplo de uso: substitua pelos caminhos desejados
    origem = "meus_arquivos"
    destino = "backup_arquivos"
    
    # Criando pasta de origem e arquivo de teste se não existirem
    if not os.path.exists(origem):
        os.makedirs(origem)
        with open(os.path.join(origem, "exemplo.txt"), "w") as f:
            f.write("Arquivo de teste para backup.")
            
    realizar_backup(origem, destino)