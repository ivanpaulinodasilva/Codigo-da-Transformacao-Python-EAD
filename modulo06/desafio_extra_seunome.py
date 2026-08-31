import json
import os
import shutil


def obter_caminhos():
    """Retorna os caminhos absolutos das pastas 'meus_arquivos' e

    'backup_arquivos' dentro do módulo 06.
    """
    pasta_modulo06 = os.path.dirname(os.path.abspath(__file__))
    pasta_origem = os.path.join(pasta_modulo06, "meus_arquivos")
    pasta_destino = os.path.join(pasta_modulo06, "backup_arquivos")
    return pasta_origem, pasta_destino


def listar_arquivos(caminho_pasta, nome_exibicao):
    """Lista e exibe os arquivos presentes em um diretório."""
    print(f"\n--- Conteúdo da pasta '{nome_exibicao}' ---")
    if not os.path.exists(caminho_pasta):
        print("⚠️ A pasta ainda não existe.")
        return []

    arquivos = [
        f
        for f in os.listdir(caminho_pasta)
        if os.path.isfile(os.path.join(caminho_pasta, f))
    ]
    if not arquivos:
        print("ℹ️ A pasta está vazia.")
    else:
        for idx, arquivo in enumerate(arquivos, start=1):
            print(f"  {idx}. 📄 {arquivo}")
    return arquivos


def editar_arquivo_backup():
    """Permite selecionar e alterar o conteúdo de um arquivo salvo em

    'backup_arquivos'.
    """
    _, pasta_destino = obter_caminhos()
    arquivos = listar_arquivos(pasta_destino, "backup_arquivos")

    if not arquivos:
        return

    escolha = input(
        "\nDigite o número do arquivo que deseja alterar (ou 0 para cancelar): "
    ).strip()
    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(arquivos):
        print("Operação cancelada ou opção inválida.")
        return

    arquivo_selecionado = arquivos[int(escolha) - 1]
    caminho_completo = os.path.join(pasta_destino, arquivo_selecionado)

    # Exibe o conteúdo atual
    print(f"\n--- Conteúdo Atual de '{arquivo_selecionado}' ---")
    with open(caminho_completo, "r", encoding="utf-8") as f:
        print(f.read())

    # Opções de edição
    print("\nComo deseja alterar o arquivo?")
    print("1. Adicionar conteúdo ao final (Append)")
    print("2. Sobrescrever todo o conteúdo (Overwrite)")
    modo_opcao = input("Escolha (1 ou 2): ").strip()

    modo = "a" if modo_opcao == "1" else "w" if modo_opcao == "2" else None

    if not modo:
        print("❌ Opção de edição inválida.")
        return

    novo_texto = input("\nDigite o novo texto/dados a serem inseridos:\n")

    with open(caminho_completo, modo, encoding="utf-8") as f:
        if modo == "a":
            f.write("\n" + novo_texto)
        else:
            f.write(novo_texto)

    print(
        f"\n✅ Arquivo '{arquivo_selecionado}' alterado com sucesso em 'backup_arquivos'!"
    )


def executar_backup():
    """Realiza a cópia dos arquivos de 'meus_arquivos' para

    'backup_arquivos'.
    """
    pasta_origem, pasta_destino = obter_caminhos()

    if not os.path.exists(pasta_origem):
        print(f"\n❌ Erro: A pasta '{pasta_origem}' não existe.")
        return

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    arquivos = os.listdir(pasta_origem)
    if not arquivos:
        print("\n⚠️ Pasta de origem vazia.")
        return

    print("\n🚀 Copiando arquivos...")
    for arquivo in arquivos:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        if os.path.isfile(caminho_origem):
            shutil.copy2(caminho_origem, caminho_destino)
            print(f"  ✓ Copiado: {arquivo}")

    print("\n✅ Backup concluído!")


def menu_principal():
    """Gerencia a navegação do sistema interativo."""
    pasta_origem, pasta_destino = obter_caminhos()

    while True:
        print("\n" + "=" * 45)
        print("   SISTEMA DE BACKUP E GERENCIAMENTO - MODULO 06")
        print("=" * 45)
        print("1. Realizar Backup Completo")
        print("2. Ver Arquivos em 'meus_arquivos'")
        print("3. Ver Arquivos em 'backup_arquivos'")
        print("4. Editar/Alterar Arquivo do Backup")
        print("5. Sair")
        print("=" * 45)

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            executar_backup()
        elif opcao == "2":
            listar_arquivos(pasta_origem, "meus_arquivos")
        elif opcao == "3":
            listar_arquivos(pasta_destino, "backup_arquivos")
        elif opcao == "4":
            editar_arquivo_backup()
        elif opcao == "5":
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Digite um número de 1 a 5.")


if __name__ == "__main__":
    menu_principal()