# ==============================================================================
# MÓDULO: utilidades.py
# Descrição: Módulo com funções para operações aritméticas e estatísticas.
# ==============================================================================

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a diferença entre dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna o produto de dois números."""
    return a * b

def dividir(a, b):
    """Retorna o quociente da divisão ou mensagem em caso de divisor zero."""
    if b == 0:
        return "Erro: Divisão por Zero não Permitida"
    return a / b

def divisao_inteira(a, b):
    """Retorna a parte inteira da divisão."""
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a // b

def resto_divisao(a, b):
    """Retorna o resto da divisão (módulo)."""
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a % b

def potencia(base, expoente):
    """Calcula a potenciação de uma base por um expoente."""
    return base ** expoente

def calcular_media(lista_numeros):
    """Calcula a média aritmética dos valores de uma lista."""
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

def e_par(numero):
    """Verifica se um número é par."""
    return numero % 2 == 0