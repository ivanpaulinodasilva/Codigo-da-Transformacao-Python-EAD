import os
import shutil


def realizar_backup_modulo06():
    """Localiza a pasta atual (modulo06), cria uma pasta 'backup_arquivos'

    dentro dela e copia todos os arquivos de dados (.txt, .json, .csv, etc.).
    """
    # 1. Obtém o caminho absoluto do diretório onde este script está salvo (pasta modulo06)
    pasta_origem = os.path.dirname(os.path.abspath(__file__))

    # 2. Define o caminho da pasta de backup dentro do próprio modulo06
    pasta_destino = os.path.join(pasta_origem, "backup_arquivos")

    print(f" Pasta de Origem: {pasta_origem}")
    print(f" Pasta de Destino: {pasta_destino}\n")

    # 3. Garante que a pasta de destino seja criada, caso ainda não exista
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        print(f"Diretório de destino criado em: '{pasta_destino}'")

    # 4. Lista todos os itens presentes dentro da pasta modulo06
    itens = os.listdir(pasta_origem)

    for item in itens:
        caminho_item_origem = os.path.join(pasta_origem, item)
        caminho_item_destino = os.path.join(pasta_destino, item)

        # Copia apenas se for um arquivo e se NÃO for o próprio script de backup
        # (evita copiar pastas ou entrar em loop copiando o próprio backup)
        if os.path.isfile(caminho_item_origem):
            # Opcional: Ignorar o próprio script de backup para não duplicá-lo na pasta backup
            if item == os.path.basename(__file__):
                continue

            shutil.copy2(caminho_item_origem, caminho_item_destino)
            print(f"✓ Copiado: {item} -> backup_arquivos/")

    print("\n Backup do Módulo 06 concluído com sucesso!")


if __name__ == "__main__":
    realizar_backup_modulo06()