'''
==============================================================================
 AULA PRÁTICA: API DO TMDB COM POO E INTERFACE GRÁFICA (TKINTER)
==============================================================================
 Pré-requisito no terminal:
 pip install requests

 👥 DIVISÃO DOS PAPÉIS E REGRAS (Pair Programming):
 🧑‍💻 Driver (Piloto): 
    - Fica no teclado.
    - Escreve a sintaxe Python, declara métodos/atributos e monta o layout.
 
 🧭 Navigator (Navegador): 
    - Não toca no teclado.
    - Orienta a lógica dos métodos, a validação das entradas e as regras de POO.
 
 ⏱️ Timer: 
    - Troca obrigatória de papéis a cada 15-20 minutos.
==============================================================================
'''

import tkinter as tk
from tkinter import messagebox, ttk
import requests


class TMDBService:
  """Classe responsável por encapsular a lógica de comunicação e requisição HTTP com a API do TMDB."""

  GENEROS_TMDB = {
      28: "Ação",
      12: "Aventura",
      16: "Animação",
      35: "Comédia",
      80: "Crime",
      99: "Documentário",
      18: "Drama",
      10751: "Família",
      14: "Fantasia",
      36: "História",
      27: "Terror",
      10402: "Música",
      9648: "Mistério",
      10749: "Romance",
      878: "Ficção Científica",
      10770: "Cinema TV",
      53: "Thriller",
      10752: "Guerra",
      37: "Faroeste",
  }

  def __init__(self, api_key: str):
    self.api_key = api_key
    self.url_busca = "https://api.themoviedb.org/3/search/movie"

  def buscar_filme(self, nome_filme: str) -> dict | None:
    """Realiza a chamada à API do TMDB e retorna um dicionário com os dados do primeiro filme encontrado."""
    parametros = {
        "api_key": self.api_key,
        "query": nome_filme,
        "language": "pt-BR",
    }

    resposta = requests.get(self.url_busca, params=parametros, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    resultados = dados.get("results", [])

    if not resultados:
      return None

    filme_bruto = resultados[0]

    # Processamento e tradução dos gêneros
    ids_generos = filme_bruto.get("genre_ids", [])
    nomes_generos = [
        self.GENEROS_TMDB.get(g_id, "Outro") for g_id in ids_generos
    ]
    generos_str = (
        ", ".join(nomes_generos)
        if nomes_generos
        else "Gênero não informado"
    )

    return {
        "titulo": filme_bruto.get("title", "Título indisponível"),
        "genero": generos_str,
        "avaliacao": filme_bruto.get("vote_average", "N/A"),
        "sinopse": filme_bruto.get("overview", "Sem sinopse disponível."),
    }


class AppFilmesTMDB(tk.Tk):
  """Classe principal que gerencia a janela Tkinter e seus componentes visuais."""

  def __init__(self):
    super().__init__()

    # Configurações da Janela
    self.title("🎬 Consulta de Filmes - API TMDB")
    self.geometry("550x500")
    self.minsize(450, 400)
    self.configure(bg="#1e1e2e")

    # Instância do serviço da API (Substitua pela sua chave do TMDB)
    self.tmdb_service = TMDBService(api_key="5dfc7c8c2095938c6ed4151d7807c523")

    # Inicializa os componentes visuais
    self._criar_widgets()

  def _criar_widgets(self):
    # Título do Cabeçalho
    lbl_titulo_app = tk.Label(
        self,
        text="🎬 Buscador de Filmes TMDB",
        font=("Helvetica", 16, "bold"),
        bg="#1e1e2e",
        fg="#cba6f7",
    )
    lbl_titulo_app.pack(pady=15)

    # Frame para Entrada de Texto e Botão
    frame_busca = tk.Frame(self, bg="#1e1e2e")
    frame_busca.pack(padx=20, fill="x", pady=5)

    lbl_instrucao = tk.Label(
        frame_busca,
        text="Nome do filme:",
        font=("Helvetica", 10),
        bg="#1e1e2e",
        fg="#cdd6f4",
    )
    lbl_instrucao.pack(anchor="w", pady=2)

    self.ent_filme = tk.Entry(
        frame_busca,
        font=("Helvetica", 11),
        bg="#313244",
        fg="#ffffff",
        insertbackground="white",
        relief="flat",
    )
    self.ent_filme.pack(fill="x", ipady=5, pady=5)
    self.ent_filme.bind("<Return>", lambda event: self.executar_busca())

    self.btn_buscar = tk.Button(
        frame_busca,
        text="🔍 Pesquisar Filme",
        font=("Helvetica", 10, "bold"),
        bg="#89b4fa",
        fg="#11111b",
        activebackground="#b4befe",
        cursor="hand2",
        command=self.executar_busca,
    )
    self.btn_buscar.pack(fill="x", pady=5)

    # Área de Exibição dos Resultados (Cartão Informático)
    frame_resultado = tk.LabelFrame(
        self,
        text=" Detalhes do Filme ",
        font=("Helvetica", 10, "bold"),
        bg="#181825",
        fg="#89b4fa",
        relief="groove",
        bd=2,
    )
    frame_resultado.pack(padx=20, pady=15, fill="both", expand=True)

    self.lbl_nome = tk.Label(
        frame_resultado,
        text="Título: -",
        font=("Helvetica", 11, "bold"),
        bg="#181825",
        fg="#a6e3a1",
        anchor="w",
        justify="left",
    )
    self.lbl_nome.pack(fill="x", padx=10, pady=5)

    self.lbl_genero = tk.Label(
        frame_resultado,
        text="Gênero: -",
        font=("Helvetica", 10),
        bg="#181825",
        fg="#cdd6f4",
        anchor="w",
        justify="left",
    )
    self.lbl_genero.pack(fill="x", padx=10, pady=2)

    self.lbl_avaliacao = tk.Label(
        frame_resultado,
        text="Avaliação: -",
        font=("Helvetica", 10),
        bg="#181825",
        fg="#f9e2af",
        anchor="w",
        justify="left",
    )
    self.lbl_avaliacao.pack(fill="x", padx=10, pady=2)

    # Campo de Texto com Rolagem para a Sinopse
    lbl_sinopse_titulo = tk.Label(
        frame_resultado,
        text="Sinopse:",
        font=("Helvetica", 10, "bold"),
        bg="#181825",
        fg="#cdd6f4",
        anchor="w",
    )
    lbl_sinopse_titulo.pack(fill="x", padx=10, pady=(8, 2))

    self.txt_sinopse = tk.Text(
        frame_resultado,
        font=("Helvetica", 9),
        bg="#313244",
        fg="#cdd6f4",
        wrap="word",
        height=6,
        relief="flat",
    )
    self.txt_sinopse.pack(padx=10, pady=5, fill="both", expand=True)

  def executar_busca(self):
    """Obtém a entrada do usuário, chama a classe de serviço e atualiza a interface gráfica."""
    nome_filme = self.ent_filme.get().strip()

    if not nome_filme:
      messagebox.showwarning(
          "Aviso", "Por favor, digite o nome de um filme antes de buscar!"
      )
      return

    try:
      filme = self.tmdb_service.buscar_filme(nome_filme)

      if not filme:
        messagebox.showinfo(
            "Sem Resultados",
            f"Nenhum filme foi encontrado com o nome '{nome_filme}'.",
        )
        return

      # Atualização dos rótulos e caixas da tela
      self.lbl_nome.config(text=f"🎬 Título: {filme['titulo']}")
      self.lbl_genero.config(text=f"🎭 Gênero(s): {filme['genero']}")
      self.lbl_avaliacao.config(
          text=f"⭐ Avaliação: {filme['avaliacao']}/10"
      )

      self.txt_sinopse.delete("1.0", tk.END)
      self.txt_sinopse.insert(tk.END, filme["sinopse"])

    except requests.exceptions.HTTPError as err:
      if err.response.status_code == 401:
        messagebox.showerror(
            "Erro 401",
            "Chave de API do TMDB inválida ou não configurada.\nAltere a"
            " 'SUA_CHAVE_TMDB_AQUI' no código.",
        )
      else:
        messagebox.showerror("Erro HTTP", f"Ocorreu um erro HTTP: {err}")

    except requests.exceptions.ConnectionError:
      messagebox.showerror(
          "Erro de Conexão",
          "Verifique sua conexão com a internet e tente novamente.",
      )

    except Exception as err:
      messagebox.showerror("Erro Inesperado", f"Detalhes do erro: {err}")


# Execução da Aplicação
if __name__ == "__main__":
  app = AppFilmesTMDB()
  app.mainloop()