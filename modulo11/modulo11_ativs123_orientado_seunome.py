import os
import sqlite3

# ==============================================================================
# CONFIGURAÇÃO DO DIRETÓRIO E BANCO DE DADOS
# ==============================================================================
PASTA_DESTINO = "modulo11"
NOME_BANCO = "exercicio_guiado.db"

# Cria a pasta 'modulo11' se ela ainda não existir no projeto
if not os.path.exists(PASTA_DESTINO):
    os.makedirs(PASTA_DESTINO)

# Define o caminho completo: modulo11/exercicio_guiado.db
CAMINHO_BANCO = os.path.join(PASTA_DESTINO, NOME_BANCO)


def conectar():
    """Cria e retorna a conexão com o banco SQLite na pasta 'modulo11'."""
    return sqlite3.connect(CAMINHO_BANCO)


def mensagem_orientacao(titulo, explicacao):
    """Exibe um cabeçalho explicativo formatado no terminal para orientar o usuário."""
    print("\n" + "=" * 60)
    print(f"📌 [ORIENTAÇÃO] {titulo.upper()}")
    print("=" * 60)
    print(explicacao)
    print("-" * 60)


def pausar():
    """Pausa a execução até o usuário pressionar ENTER."""
    input("\n▶ Pressione ENTER para continuar para o próximo passo...")


# ==============================================================================
# PASSO 1: Criar a Tabela
# ==============================================================================
def passo_1_criar_tabela():
    mensagem_orientacao(
        "Passo 1: Criando o Banco de Dados na pasta 'modulo11'",
        f"Nesta etapa, o programa se conecta ao banco de dados SQLite salvo em:\n"
        f"👉 '{CAMINHO_BANCO}'\n\n"
        "Se a pasta 'modulo11' ou o arquivo não existirem, eles são criados automaticamente.\n"
        "Em seguida, executa um comando SQL CREATE TABLE para criar a tabela 'Clientes'\n"
        "com as colunas: id (chave primária), nome (texto) e email (texto)."
    )
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()
    
    print(f"✓ Sucesso: Tabela 'Clientes' criada/verificada dentro de '{CAMINHO_BANCO}'!")
    pausar()


# ==============================================================================
# PASSO 2: Operações CRUD Interativas
# ==============================================================================
def passo_2_crud_inserir():
    mensagem_orientacao(
        "Passo 2.1: Operação CREATE (Inserir Clientes)",
        "Agora você vai cadastrar clientes no banco de dados.\n"
        "O programa executará o comando SQL 'INSERT INTO Clientes (nome, email) VALUES (?, ?)'."
    )
    
    qtd = input("Quantos clientes você deseja cadastrar agora? (ex: 2): ").strip()
    if not qtd.isdigit() or int(qtd) <= 0:
        qtd = 2
        print("Valor inválido. Cadastraremos 2 clientes por padrão.")
    else:
        qtd = int(qtd)

    for i in range(1, qtd + 1):
        print(f"\n--- Cadastro do Cliente {i} ---")
        nome = input(f"Digite o nome do cliente {i}: ").strip()
        email = input(f"Digite o e-mail do cliente {i}: ").strip()
        
        if nome and email:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
            conexao.commit()
            conexao.close()
            print(f"✓ Cliente '{nome}' salvo no banco em '{CAMINHO_BANCO}'!")
        else:
            print("❌ Nome ou e-mail em branco. Cadastro ignorado.")
            
    pausar()


def passo_2_crud_listar():
    mensagem_orientacao(
        "Passo 2.2: Operação READ (Consultar Dados)",
        "Vamos visualizar todos os registros inseridos na tabela até agora.\n"
        "O programa executa a consulta SQL: 'SELECT * FROM Clientes'."
    )
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    conexao.close()

    if not clientes:
        print("Nenhum cliente cadastrado até o momento.")
    else:
        print(f"{'ID':<5} | {'NOME':<25} | {'E-MAIL':<30}")
        print("-" * 65)
        for c in clientes:
            print(f"{c[0]:<5} | {c[1]:<25} | {c[2]:<30}")
            
    pausar()


def passo_2_crud_atualizar():
    mensagem_orientacao(
        "Passo 2.3: Operação UPDATE (Atualizar Registro)",
        "Nesta etapa, você pode alterar o e-mail de um cliente existente especificando seu ID.\n"
        "Comando SQL: 'UPDATE Clientes SET email = ? WHERE id = ?'."
    )
    
    id_cliente = input("Digite o ID do cliente que deseja atualizar o e-mail: ").strip()
    novo_email = input("Digite o novo e-mail para este cliente: ").strip()

    if id_cliente.isdigit() and novo_email:
        conexao = conectar()
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM Clientes WHERE id = ?", (int(id_cliente),))
        if cursor.fetchone():
            cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, int(id_cliente)))
            conexao.commit()
            print(f"✓ E-mail do cliente ID {id_cliente} atualizado com sucesso!")
        else:
            print(f"❌ Cliente com ID {id_cliente} não foi encontrado.")
            
        conexao.close()
    else:
        print("❌ ID inválido ou novo e-mail vazio. Operação cancelada.")

    pausar()


def passo_2_crud_deletar():
    mensagem_orientacao(
        "Passo 2.4: Operação DELETE (Excluir Registro)",
        "Agora você pode remover um cliente do banco através do seu ID.\n"
        "Comando SQL: 'DELETE FROM Clientes WHERE id = ?'."
    )
    
    id_cliente = input("Digite o ID do cliente que deseja excluir (ou deixe em branco para pular): ").strip()

    if id_cliente.isdigit():
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Clientes WHERE id = ?", (int(id_cliente),))
        conexao.commit()
        conexao.close()
        print(f"✓ Se existia, o cliente ID {id_cliente} foi excluído!")
    else:
        print("Etapa de exclusão ignorada.")

    pausar()


# ==============================================================================
# PASSO 3: Filtrar Dados com SQL (LIKE)
# ==============================================================================
def passo_3_filtrar_por_letra():
    mensagem_orientacao(
        "Passo 3: Filtrando Dados com SQL (Cláusula LIKE)",
        "Vamos filtrar os clientes cujo nome começa com uma determinada letra.\n"
        "Usaremos a consulta SQL: \"SELECT * FROM Clientes WHERE nome LIKE 'A%'\"\n"
        "O caractere coringa '%' busca qualquer texto após a letra especificada."
    )
    
    letra = input("Digite a letra inicial para buscar clientes (padrão: 'A'): ").strip().upper()
    if not letra:
        letra = "A"

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (f"{letra}%",))
    clientes = cursor.fetchall()
    conexao.close()

    print(f"\n--- CLIENTES COM NOME COMEÇANDO EM '{letra}' ---")
    if not clientes:
        print(f"Nenhum cliente encontrado com a inicial '{letra}'.")
    else:
        for c in clientes:
            print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")
            
    pausar()


# ==============================================================================
# FLUXO PRINCIPAL ORIENTADO DO PROGRAMA
# ==============================================================================
def executar_programa_orientado():
    print("\n" + "=" * 60)
    print(" 🚀 BEM-VINDO AO PROGRAMA ORIENTADO DE SQLITE E PYTHON")
    print("=" * 60)
    print(f"Diretório do banco de dados: '{CAMINHO_BANCO}'")
    print("Este programa vai guiá-lo passo a passo na criação e manipulação")
    print("de um banco de dados relacional para cumprir os itens 1, 2 e 3.")
    pausar()

    passo_1_criar_tabela()
    passo_2_crud_inserir()
    passo_2_crud_listar()
    passo_2_crud_atualizar()
    passo_2_crud_listar()
    passo_2_crud_deletar()
    passo_2_crud_listar()
    passo_3_filtrar_por_letra()

    print("\n" + "=" * 60)
    print(" 🎉 PARABÉNS! Você concluiu todas as etapas dos Itens 1, 2 e 3!")
    print("=" * 60)


if __name__ == "__main__":
    executar_programa_orientado()