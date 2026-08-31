# ==========================================
# ATIVIDADE 03: Validação de Entrada de Usuário
# ==========================================

def solicitar_idade_valida():
    """
    Solicita a idade do usuário e valida se a entrada é um número inteiro positivo.
    
    Retorna:
    - int: A idade validada do usuário.
    """
    while True:
        # Recebe a entrada do usuário como texto
        entrada = input("Por favor, digite a sua idade: ")
        
        try:
            # Tenta converter o texto digitado para um número inteiro
            idade = int(entrada)
            
            # Validação da regra de negócio: idade deve ser maior que zero
            if idade <= 0:
                print("Erro: A idade deve ser um número inteiro positivo (maior que zero).\n")
                continue # Volta para o início do loop para pedir a entrada novamente
            
            # Se passou pelas validações, retorna a idade e encerra a função
            return idade

        except ValueError:
            # Captura o erro caso a conversão int(entrada) falhe (ex: se o usuário digitar letras)
            print("Erro: Entrada inválida! Por favor, digite apenas números inteiros.\n")


# ==========================================
# EXECUÇÃO E TESTES DO CÓDIGO
# ==========================================
if __name__ == "__main__":
    print("--- Teste da Atividade 3: Validação de Idade ---\n")
    
    # Chama a função e armazena o resultado validado
    idade_confirmada = solicitar_idade_valida()
    
    print(f"\nSucesso! Idade de {idade_confirmada} anos registrada no sistema.")