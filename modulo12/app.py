from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota para somar dois números
@app.route("/somar", methods=["POST"])
def somar():
    dados = request.get_json()
    if not dados or "a" not in dados or "b" not in dados:
        return jsonify({"erro": "Parâmetros 'a' e 'b' são obrigatórios."}), 400
    
    try:
        a = float(dados["a"])
        b = float(dados["b"])
    except (ValueError, TypeError):
        return jsonify({"erro": "Os valores devem ser números válidos."}), 400

    return jsonify({"resultado": a + b}), 200

# Rota para dividir dois números
@app.route("/dividir", methods=["POST"])
def dividir():
    dados = request.get_json()
    if not dados or "a" not in dados or "b" not in dados:
        return jsonify({"erro": "Parâmetros 'a' e 'b' são obrigatórios."}), 400

    try:
        a = float(dados["a"])
        b = float(dados["b"])
    except (ValueError, TypeError):
        return jsonify({"erro": "Os valores devem ser números válidos."}), 400

    if b == 0:
        return jsonify({"erro": "Divisão por zero não é permitida."}), 400

    return jsonify({"resultado": a / b}), 200

if __name__ == "__main__":
    app.run(debug=True)