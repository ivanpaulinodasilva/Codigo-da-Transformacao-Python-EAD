'''



'''

import random
import math

def jogar():
    limite_inferior = 1
    limite_superior = 24
    
    # Gerando número secreto aleatório
    numero_secreto = random.randint(limite_inferior, limite_superior)
    
    # Calculando o número máximo de tentativas com fórmula matemática (log2)
    max_tentativas = math.ceil(math.log2(limite_superior - limite_inferior + 1))
    
    print("=== JOGO DA ADIVINHAÇÃO ===")
    print(f"Tente adivinhar o número entre {limite_inferior} e {limite_superior}.")
    print(f"Você tem {max_tentativas} tentativas!\n")

    tentativas = 0
    while tentativas < max_tentativas:
        palpite = int(input(f"Tentativa {tentativas + 1}: Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
            break
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")
    else:
        print(f"\nFim de jogo! O número era {numero_secreto}.")

if __name__ == "__main__":
    jogar()