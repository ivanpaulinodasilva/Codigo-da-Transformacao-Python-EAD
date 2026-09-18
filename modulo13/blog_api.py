'''
pip install flask
pip install flask flask-jwt-extended


'''

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import sqlite3

app = Flask(__name__)

# Configuração do JWT
app.config["JWT_SECRET_KEY"] = "minha_chave_secreta_super_segura"
jwt = JWTManager(app)

# --- BANCO DE DADOS DO BLOG ---
def init_blog_db():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    
    # Tabela de Autenticação/Usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    
    # Tabela de Posts do Blog
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES usuarios (id)
        )
    """)
    conn.commit()
    conn.close()

init_blog_db()

# --- AUTENTICAÇÃO ---

# Registro de Usuários
@app.route("/auth/register", methods=["POST"])
def register():
    dados = request.get_json()
    username = dados.get("username")
    senha = dados.get("senha")

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?)", (username, senha))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"erro": "Usuário já existe"}), 400

    conn.close()
    return jsonify({"mensagem": "Usuário registrado com sucesso"}), 201

# Login (Geração de Token)
@app.route("/auth/login", methods=["POST"])
def login():
    dados = request.get_json()
    username = dados.get("username")
    senha = dados.get("senha")

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE username = ? AND senha = ?", (username, senha))
    user = cursor.fetchone()
    conn.close()

    if user:
        access_token = create_access_token(identity=str(user[0]))
        return jsonify({"token": access_token}), 200

    return jsonify({"erro": "Credenciais inválidas"}), 401


# --- FUNCIONALIDADES DO BLOG ---

# Criar Post (Exige Autenticação JWT)
@app.route("/posts", methods=["POST"])
@jwt_required()
def criar_post():
    autor_id = get_jwt_identity()
    dados = request.get_json()
    titulo = dados.get("titulo")
    conteudo = dados.get("conteudo")

    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)",
        (titulo, conteudo, autor_id)
    )
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()

    return jsonify({"mensagem": "Post criado!", "id": post_id}), 201

# Listar Todos os Posts (Público)
@app.route("/posts", methods=["GET"])
def listar_posts():
    conn = sqlite3.connect("blog.db")
    cursor = conn.cursor()
    cursor.execute("SELECT posts.id, posts.titulo, posts.conteudo, usuarios.username FROM posts JOIN usuarios ON posts.autor_id = usuarios.id")
    posts = cursor.fetchall()
    conn.close()

    lista_posts = [
        {"id": p[0], "titulo": p[1], "conteudo": p[2], "autor": p[3]}
        for p in posts
    ]
    return jsonify({"posts": lista_posts}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)