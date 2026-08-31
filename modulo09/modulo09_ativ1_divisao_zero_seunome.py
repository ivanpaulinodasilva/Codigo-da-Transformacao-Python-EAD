def calculadora_divisao(numerador, denominador):
    """
    Função para realizar a divisão de dois números com tratamento de erros.
    
    Parâmetros:
    - numerador (float/int): O número que será dividido.
    - denominador (float/int): O número pelo qual vamos dividir.
    """
    try:
        # Tenta realizar a divisão normalmente
        resultado = numerador / denominador
        return f"Resultado da divisão: {resultado}"
        
    except ZeroDivisionError:
        # Este bloco é executado caso o denominador seja 0
        return "Erro: Não é possível realizar divisão por zero!"

# ==========================================
# TESTES E EXECUÇÃO
# ==========================================

# Teste 1: Divisão normal
print("--- Teste 1 ---")
print(calculadora_divisao(10, 2))

# Teste 2: Tentativa de divisão por zero
print("\n--- Teste 2 ---")
print(calculadora_divisao(10, 0))