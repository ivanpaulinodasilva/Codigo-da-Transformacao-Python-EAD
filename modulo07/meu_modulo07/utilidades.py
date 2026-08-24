'''
Potenciação

Divisão

Multiplicação

Soma

Subtração
'''


def soma(a, b):

    return a + b


def subtrair(a, b):

    return a - b


def multiplicar(a,b):

    return a * b


def dividir(a,b):

    if b == 0:
        return "Erro: Divisão por Zero não Permitida"
    return a / b

    
def divisao_inteira(a, b):
    """
    Retorna apenas a parte inteira da divisão de 'a' por 'b'.
    Parâmetros: a (int/float), b (int/float)
    Retorno: O quociente inteiro ou uma mensagem de erro se b == 0.
    """
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a // b


def resto_divisao(a, b):
    """
    Calcula o resto da divisão (módulo) de 'a' por 'b'.
    Parâmetros: a (int/float), b (int/float)
    Retorno: O resto da divisão ou uma mensagem de erro se b == 0.
    """
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a % b


def potencia(base, expoente):
    """
    Eleva a base ao expoente (potenciação).
    Parâmetros: base (int/float), expoente (int/float)
    Retorno: O resultado de base elevado ao expoente.
    """
    return base ** expoente


def calcular_media(lista_numeros):

    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


def e_par(numero):
    return numero % 2 == 0
