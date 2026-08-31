# ==============================================================================
# MÓDULO: jogo_adivinhacao.py
# Descrição: Responsável pela lógica do jogo de adivinhação usando Random e Math.
# ==============================================================================

import random
import math

def iniciar_jogo_adivinhacao():
    """
    Executa o jogo de adivinhação com limite de tentativas calculado via log2.
    """
    limite_min = 1
    limite_max = 50
    numero_secreto = random.randint(limite_min, limite_max)
    
    # Cálculo matemático de tentativas ideais: log2(intervalo)
    max_tentativas = math.ceil(math.log2(limite_max - limite_min + 1))
    
    print("\n--- DESAFIO DE MATEMÁTICA: ADIVINHE O NÚMERO ---")
    print(f"Tente adivinhar o número entre {limite_min} e {limite_max}.")
    print(f"Você tem {max_tentativas} tentativas!")

    for tentativa in range(1, max_tentativas + 1):
        try:
            palpite = int(input(f"Tentativa {tentativa}: "))
        except ValueError:
            print("Por favor, digite apenas números inteiros válidos!")
            continue

        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            return True
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")
            
    print(f"\nFim de jogo! O número era {numero_secreto}.")
    return False