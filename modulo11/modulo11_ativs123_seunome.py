import sqlite3

def conectar():
    """Cria a conexão com o banco de dados SQLite."""
    return sqlite3.connect("exercicio.db")

# ==============================================================================
# ITEM 1: Configuração do Banco de Dados e Criação da Tabela Clientes
# ==============================================================================
def criar_tabela():
    """Configura o banco de dados e cria a tabela Clientes."""
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
    print("✓ Tabela 'Clientes' configurada com sucesso!")

# ==============================================================================
# ITEM 2: Operações CRUD (Create, Read, Update, Delete)
# ==============================================================================

# CREATE - Inserir Cliente
def inserir_cliente(nome, email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()
    print(f"✓ Cliente '{nome}' inserido.")

# READ - Listar Todos os Clientes
def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    conexao.close()

    print("\n--- LISTA DE CLIENTES ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for c in clientes:
            print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")

# UPDATE - Atualizar E-mail do Cliente
def atualizar_email_cliente(id_cliente, novo_email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    conexao.commit()
    conexao.close()
    print(f"\n✓ E-mail do cliente ID {id_cliente} atualizado para '{novo_email}'.")

# DELETE - Excluir Cliente
def deletar_cliente(id_cliente):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    conexao.close()
    print(f"\n✓ Cliente ID {id_cliente} deletado.")

# ==============================================================================
# ITEM 3: Filtro de Dados com SQL (Busca nomes que começam com 'A')
# ==============================================================================
def filtrar_clientes_por_letra(letra="A"):
    conexao = conectar()
    cursor = conexao.cursor()
    
    # O operador LIKE com 'A%' busca registros iniciados na letra desejada
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (f"{letra}%",))
    clientes = cursor.fetchall()
    conexao.close()

    print(f"\n--- FILTRO: CLIENTES COMEÇANDO COM '{letra}' ---")
    if not clientes:
        print(f"Nenhum cliente encontrado com a letra '{letra}'.")
    else:
        for c in clientes:
            print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")

# ==============================================================================
# EXECUÇÃO COMPLETA DAS ATIVIDADES 1, 2 E 3
# ==============================================================================
if __name__ == "__main__":
    # Item 1: Criar tabela
    criar_tabela()

    # Item 2: Operações CRUD
    print("\n1. [CREATE] Inserindo clientes...")
    inserir_cliente("Ana Silva", "ana@email.com")
    inserir_cliente("Bruno Costa", "bruno@email.com")
    inserir_cliente("Amanda Souza", "amanda@email.com")
    inserir_cliente("Carlos Oliveira", "carlos@email.com")

    print("\n2. [READ] Consultando todos os clientes...")
    listar_clientes()

    print("\n3. [UPDATE] Atualizando e-mail do cliente ID 2...")
    atualizar_email_cliente(2, "bruno.costa@novodominio.com")
    listar_clientes()

    print("\n4. [DELETE] Excluindo cliente ID 4...")
    deletar_cliente(4)
    listar_clientes()

    # Item 3: Filtro SQL
    filtrar_clientes_por_letra("A")