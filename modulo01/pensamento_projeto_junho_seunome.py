# =================================================================
# CURSO DE PROGRAMAÇÃO - SISTEMA AÇAITERIA (GUI - TKINTER)
# Módulo: Transição de CLI para Interface Gráfica com Inputs e Estoque Brancos
# =================================================================

import tkinter as tk
from tkinter import messagebox

# --- PALETA DE CORES PERSONALIZADA ---
COR_AZUL_ESCURO = "#004d6e"   # AE
COR_AZUL_MEDIO  = "#0081ab"   # AM
COR_AZUL_CLARO  = "#00b1cd"   # AC
COR_VERDE       = "#a6c844"   # V
COR_ROXO_VINHO  = "#b83764"   # R
COR_AMARELO     = "#edce01"   # A
COR_MARROM_DARK = "#4a3336"   # B

# --- ESTADO INICIAL DO SISTEMA (Variáveis Solicitadas) ---
p1_nome = "açaí comum"
p1_estoque = 100
p1_preco = 8.90
p1_validade = "10/12/2026"
p1_descricao = "Açaí comum, ideal para quem gosta de um sabor clássico."

p2_nome = "açaí guarana"
p2_estoque = 50
p2_preco = 12.90
p2_validade = "10/10/2026"
p2_descricao = "Açaí guarana, com sabor refrescante e ingredientes de qualidade."

p3_nome = "açaí cupuaçu"
p3_estoque = 130
p3_preco = 15.90
p3_validade = "10/12/2026"
p3_descricao = "Açaí cupuaçu, com ingredientes locais e sabor autêntico."


# --- FUNÇÕES DE LÓGICA DO SISTEMA ---

def atualizar_lista_produtos():
    """Atualiza o campo de texto exibindo os produtos cadastrados."""
    txt_lista.delete("1.0", tk.END)  # Limpa o campo de texto
    
    if p1_nome == "" and p2_nome == "" and p3_nome == "":
        txt_lista.insert(tk.END, "Nenhum produto cadastrado no sistema ainda.\n")
        return

    # Mostrar Produto 1
    if p1_nome != "":
        txt_lista.insert(tk.END, f"Nome: {p1_nome.upper()} | Preço: R$ {p1_preco:.2f} | Estoque: {p1_estoque} unid.\n")
        txt_lista.insert(tk.END, f"Validade: {p1_validade} | Descrição: {p1_descricao}\n")
        txt_lista.insert(tk.END, "-" * 60 + "\n")
        
    # Mostrar Produto 2
    if p2_nome != "":
        txt_lista.insert(tk.END, f"Nome: {p2_nome.upper()} | Preço: R$ {p2_preco:.2f} | Estoque: {p2_estoque} unid.\n")
        txt_lista.insert(tk.END, f"Validade: {p2_validade} | Descrição: {p2_descricao}\n")
        txt_lista.insert(tk.END, "-" * 60 + "\n")
        
    # Mostrar Produto 3
    if p3_nome != "":
        txt_lista.insert(tk.END, f"Nome: {p3_nome.upper()} | Preço: R$ {p3_preco:.2f} | Estoque: {p3_estoque} unid.\n")
        txt_lista.insert(tk.END, f"Validade: {p3_validade} | Descrição: {p3_descricao}\n")
        txt_lista.insert(tk.END, "-" * 60 + "\n")

def cadastrar_produto():
    """Lógica da Opção 1: Cadastrar Produto"""
    global p1_nome, p1_estoque, p1_preco, p1_validade, p1_descricao
    global p2_nome, p2_estoque, p2_preco, p2_validade, p2_descricao
    global p3_nome, p3_estoque, p3_preco, p3_validade, p3_descricao

    nome = entry_nome.get()
    
    try:
        estoque = int(entry_estoque.get())
        preco = float(entry_preco.get())
    except ValueError:
        messagebox.showerror("Erro", "Estoque deve ser inteiro e Preço deve ser numérico!")
        return

    validade = entry_validade.get()
    descricao = entry_descricao.get()

    if nome == "":
        messagebox.showwarning("Aviso", "O nome do produto não pode ser vazio!")
        return

    # Verificação de vagas disponíveis
    if p1_nome == "":
        p1_nome, p1_estoque, p1_preco, p1_validade, p1_descricao = nome, estoque, preco, validade, descricao
        messagebox.showinfo("Sucesso", f'Produto "{p1_nome}" cadastrado na vaga 1!')
    elif p2_nome == "":
        p2_nome, p2_estoque, p2_preco, p2_validade, p2_descricao = nome, estoque, preco, validade, descricao
        messagebox.showinfo("Sucesso", f'Produto "{p2_nome}" cadastrado na vaga 2!')
    elif p3_nome == "":
        p3_nome, p3_estoque, p3_preco, p3_validade, p3_descricao = nome, estoque, preco, validade, descricao
        messagebox.showinfo("Sucesso", f'Produto "{p3_nome}" cadastrado na vaga 3!')
    else:
        messagebox.showerror("Limite Atingido", "Sistema cheio! Limite de 3 produtos atingido.")
        return

    # Limpar campos do formulário
    entry_nome.delete(0, tk.END)
    entry_estoque.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    entry_validade.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    
    atualizar_lista_produtos()

def realizar_venda():
    """Lógica da Opção 3: Realizar Venda"""
    global p1_estoque, p2_estoque, p3_estoque

    nome_venda = entry_venda_nome.get().strip()
    try:
        qtd_venda = int(entry_venda_qtd.get())
    except ValueError:
        messagebox.showerror("Erro", "Digite uma quantidade válida para a venda.")
        return

    if p1_nome == "" and p2_nome == "" and p3_nome == "":
        messagebox.showwarning("Aviso", "Não há produtos cadastrados para realizar vendas.")
        return

    # Teste de venda contra os produtos existentes
    if nome_venda.lower() == p1_nome.lower() and p1_nome != "":
        if qtd_venda <= p1_estoque:
            p1_estoque -= qtd_venda
            total = qtd_venda * p1_preco
            messagebox.showinfo("Venda Concluída", f"Venda realizada!\nTotal: R$ {total:.2f}\nEstoque atual: {p1_estoque}")
        else:
            messagebox.showwarning("Erro de Estoque", f"Estoque insuficiente! Temos apenas {p1_estoque}.")
            
    elif nome_venda.lower() == p2_nome.lower() and p2_nome != "":
        if qtd_venda <= p2_estoque:
            p2_estoque -= qtd_venda
            total = qtd_venda * p2_preco
            messagebox.showinfo("Venda Concluída", f"Venda realizada!\nTotal: R$ {total:.2f}\nEstoque atual: {p2_estoque}")
        else:
            messagebox.showwarning("Erro de Estoque", f"Estoque insuficiente! Temos apenas {p2_estoque}.")
            
    elif nome_venda.lower() == p3_nome.lower() and p3_nome != "":
        if qtd_venda <= p3_estoque:
            p3_estoque -= qtd_venda
            total = qtd_venda * p3_preco
            messagebox.showinfo("Venda Concluída", f"Venda realizada!\nTotal: R$ {total:.2f}\nEstoque atual: {p3_estoque}")
        else:
            messagebox.showwarning("Erro de Estoque", f"Estoque insuficiente! Temos apenas {p3_estoque}.")
    else:
        messagebox.showerror("Erro", "Produto não encontrado!")
        return

    entry_venda_nome.delete(0, tk.END)
    entry_venda_qtd.delete(0, tk.END)
    atualizar_lista_produtos()


# --- CONFIGURAÇÃO DA JANELA PRINCIPAL (INTERFACE) ---
janela = tk.Tk()
janela.title("Sistema de Vendas - Açaiteria")
janela.geometry("750x650")
janela.configure(bg=COR_AZUL_ESCURO) # Fundo Geral: AE

# Título Principal
lbl_titulo = tk.Label(janela, text="Bem-vindo à Açaiteria!", font=("Arial", 18, "bold"), bg=COR_AZUL_ESCURO, fg=COR_AMARELO)
lbl_titulo.pack(pady=10)

# --- FRAME: CADASTRO DE PRODUTOS ---
frame_cadastro = tk.LabelFrame(janela, text=" 1 - Cadastrar Produto ", font=("Arial", 11, "bold"), bg=COR_AZUL_MEDIO, fg=COR_VERDE, padx=10, pady=10)
frame_cadastro.pack(fill="x", padx=15, pady=5)

tk.Label(frame_cadastro, text="Nome:", bg=COR_AZUL_MEDIO, fg="white").grid(row=0, column=0, sticky="w")
entry_nome = tk.Entry(frame_cadastro, width=25, bg="white", fg=COR_MARROM_DARK, insertbackground="black")
entry_nome.grid(row=0, column=1, padx=5, pady=2)

tk.Label(frame_cadastro, text="Estoque:", bg=COR_AZUL_MEDIO, fg="white").grid(row=0, column=2, sticky="w")
entry_estoque = tk.Entry(frame_cadastro, width=10, bg="white", fg=COR_MARROM_DARK, insertbackground="black")
entry_estoque.grid(row=0, column=3, padx=5, pady=2)

tk.Label(frame_cadastro, text="Preço:", bg=COR_AZUL_MEDIO, fg="white").grid(row=1, column=0, sticky="w")
entry_preco = tk.Entry(frame_cadastro, width=25, bg="white", fg=COR_MARROM_DARK, insertbackground="black")
entry_preco.grid(row=1, column=1, padx=5, pady=2)

tk.Label(frame_cadastro, text="Validade:", bg=COR_AZUL_MEDIO, fg="white").grid(row=1, column=2, sticky="w")
entry_validade = tk.Entry(frame_cadastro, width=10, bg="white", fg=COR_MARROM_DARK, insertbackground="black")
entry_validade.grid(row=1, column=3, padx=5, pady=2)

tk.Label(frame_cadastro, text="Descrição:", bg=COR_AZUL_MEDIO, fg="white").grid(row=2, column=0, sticky="w")
entry_descricao = tk.Entry(frame_cadastro, width=45, bg="white", fg=COR_MARROM_DARK, insertbackground="black")
entry_descricao.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="w")

btn_cadastrar = tk.Button(frame_cadastro, text="Salvar Produto", command=cadastrar_produto, bg=COR_VERDE, fg=COR_MARROM_DARK, font=("Arial", 10, "bold"))
btn_cadastrar.grid(row=3, column=0, columnspan=4, pady=5)

# --- FRAME: REALIZAR VENDA ---
frame_venda = tk.LabelFrame(janela, text=" 3 - Realizar Venda ", font=("Arial", 11, "bold"), bg=COR_AZUL_MEDIO, fg=COR_AMARELO, padx=10, pady=10)
frame_venda.pack(fill="x", padx=15, pady=5)

tk.Label(frame_venda, text="Nome do Produto:", bg=COR_AZUL_MEDIO, fg="white").grid(row=0, column=0, sticky="w")
entry_venda_nome = tk.Entry(frame_venda, width=25, bg="white", fg=COR_MARROM_DARK, insertbackground="black")
entry_venda_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_venda, text="Quantidade:", bg=COR_AZUL_MEDIO, fg="white").grid(row=0, column=2, sticky="w")
entry_venda_qtd = tk.Entry(frame_venda, width=10, bg="white", fg=COR_MARROM_DARK, insertbackground="black")
entry_venda_qtd.grid(row=0, column=3, padx=5, pady=5)

btn_vender = tk.Button(frame_venda, text="Confirmar Venda", command=realizar_venda, bg=COR_ROXO_VINHO, fg="white", font=("Arial", 10, "bold"))
btn_vender.grid(row=0, column=4, padx=15)

# --- FRAME: LISTAGEM DE PRODUTOS ---
frame_lista = tk.LabelFrame(janela, text=" 2 - Produtos em Estoque ", font=("Arial", 11, "bold"), bg=COR_AZUL_MEDIO, fg=COR_AZUL_CLARO, padx=10, pady=10)
frame_lista.pack(fill="both", expand=True, padx=15, pady=5)

# Fundo alterado para branco ("white") e letras alteradas para a cor marrom escura para excelente leitura do estoque
txt_lista = tk.Text(frame_lista, height=10, font=("Courier New", 10, "bold"), bg="white", fg=COR_MARROM_DARK)
txt_lista.pack(fill="both", expand=True)

# Inicializar a tela mostrando os dados pré-carregados
atualizar_lista_produtos()

# Executa o loop do aplicativo
janela.mainloop()