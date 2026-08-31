# ==========================================
# 1. Definição da Exceção Personalizada
# ==========================================
class SaldoInsuficienteError(Exception):
    """
    Exceção personalizada lançada quando o valor do saque 
    é maior do que o saldo disponível na conta bancária.
    """
    pass


# ==========================================
# 2. Definição da Classe da Conta Bancária
# ==========================================
class ContaBancaria:
    def __init__(self, saldo_inicial):
        """
        Inicializa a conta bancária com um saldo inicial.
        
        Parâmetro:
        - saldo_inicial (float/int): O valor inicial disponível na conta.
        """
        self.saldo = saldo_inicial

    def sacar(self, valor):
        """
        Realiza um saque na conta se houver saldo suficiente.
        
        Parâmetro:
        - valor (float/int): O valor a ser retirado.
        """
        # Verifica se o valor solicitado é maior que o saldo atual
        if valor > self.saldo:
            # Lança (raise) a exceção personalizada se o saldo for insuficiente
            raise SaldoInsuficienteError(
                f"Saque negado! Valor solicitado: R$ {valor:.2f} | Saldo disponível: R$ {self.saldo:.2f}"
            )
        
        # Caso haja saldo, realiza a subtração e atualiza a conta
        self.saldo -= valor
        return f"Saque de R$ {valor:.2f} realizado com sucesso! Saldo restante: R$ {self.saldo:.2f}"


# ==========================================
# 3. Testes e Execução do Código
# ==========================================
if __name__ == "__main__":
    # Criamos uma conta com R$ 100,00 de saldo inicial
    minha_conta = ContaBancaria(saldo_inicial=100.0)

    # Teste 1: Saque permitido (dentro do saldo)
    print("--- Teste 1: Saque Permitido ---")
    try:
        mensagem_sucesso = minha_conta.sacar(40.0)
        print(mensagem_sucesso)
    except SaldoInsuficienteError as erro:
        print(f"Erro: {erro}")

    # Teste 2: Saque negado (maior do que o saldo restante de R$ 60,00)
    print("\n--- Teste 2: Saque Sem Saldo ---")
    try:
        mensagem_sucesso = minha_conta.sacar(100.0)
        print(mensagem_sucesso)
    except SaldoInsuficienteError as erro:
        # Captura especificamente a exceção que nós criamos
        print(f"Erro capturado: {erro}")