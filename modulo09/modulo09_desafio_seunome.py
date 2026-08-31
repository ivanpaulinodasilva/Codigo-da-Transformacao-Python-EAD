# ==========================================
# 1. EXCEÇÕES PERSONALIZADAS (Camada de Domínio)
# ==========================================
class CredenciaisInvalidasError(Exception):
    """Exceção para usuário ou senha incorretos."""
    pass

class LimiteTentativasExcedidoError(Exception):
    """Exceção para quando o usuário excede o número máximo de tentativas."""
    pass


# ==========================================
# 2. SERVIÇO DE AUTENTICAÇÃO (Camada de Serviço)
# ==========================================
class AuthService:
    def __init__(self, usuario_valido="admin", senha_valida="admin123", max_tentativas=3):
        """
        Inicializa o serviço com credenciais padrão e limite de tentativas.
        """
        self._usuario_valido = usuario_valido
        self._senha_valida = senha_valida
        self.max_tentativas = max_tentativas
        self.tentativas_atuais = 0

    def autenticar(self, usuario, senha):
        """
        Valida as credenciais fornecidas.
        
        Lança:
        - LimiteTentativasExcedidoError: Se o limite de falhas já foi atingido.
        - CredenciaisInvalidasError: Se usuário ou senha estiverem incorretos.
        """
        # Verifica se o limite de tentativas já foi atingido
        if self.tentativas_atuais >= self.max_tentativas:
            raise LimiteTentativasExcedidoError("Conta bloqueada temporariamente por segurança.")

        # Valida usuário e senha
        if usuario != self._usuario_valido or senha != self._senha_valida:
            self.tentativas_atuais += 1
            tentativas_restantes = self.max_tentativas - self.tentativas_atuais
            
            if self.tentativas_atuais >= self.max_tentativas:
                raise LimiteTentativasExcedidoError("Acesso bloqueado! Limite máximo de tentativas atingido.")
            
            raise CredenciaisInvalidasError(
                f"Credenciais incorretas. Tentativas restantes: {tentativas_restantes}"
            )

        # Se as credenciais estiverem corretas, reseta o contador
        self.tentativas_atuais = 0
        return True


# ==========================================
# 3. INTERFACE DE TERMINAL (Camada de Aplicação)
# ==========================================
def executar_interface_login():
    """
    Controla o fluxo de telas no terminal para interação com o usuário.
    """
    auth_system = AuthService(usuario_valido="dev_user", senha_valida="pass123", max_tentativas=3)
    
    print("==========================================")
    print("      SISTEMA DE AUTENTICAÇÃO - DEV       ")
    print("==========================================")
    
    while True:
        try:
            usr = input("\n[LOGIN] Usuário: ")
            pwd = input("[LOGIN] Senha:   ")
            
            # Tenta autenticar no serviço
            if auth_system.autenticar(usr, pwd):
                print("\n[OK] Autenticação bem-sucedida! Acessando o painel...")
                break
                
        except CredenciaisInvalidasError as e:
            # Captura falha de senha/usuário
            print(f"[ERRO] {e}")
            
        except LimiteTentativasExcedidoError as e:
            # Captura o bloqueio do sistema
            print(f"\n[BLOQUEADO] {e}")
            print("Encerrando a sessão...")
            break


# ==========================================
# EXECUÇÃO DO SISTEMA
# ==========================================
if __name__ == "__main__":
    executar_interface_login()