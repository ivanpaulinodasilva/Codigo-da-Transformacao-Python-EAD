import unittest

# =========================================================
# Código da Aplicação (O que será testado)
# =========================================================

def somar_funcao(a, b):
    """Função simples de soma para o Item 1."""
    return a + b


class Calculadora:
    """Classe Calculadora para os Itens 2 e 3."""
    
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b


# =========================================================
# Suíte de Testes (unittest)
# =========================================================

class TestesCalculadora(unittest.TestCase):

    # -----------------------------------------------------
    # Item 1: Teste para a função simples de soma
    # -----------------------------------------------------
    def test_somar_funcao(self):
        resultado = somar_funcao(3, 5)
        self.assertEqual(resultado, 8)

    # -----------------------------------------------------
    # Item 2: Testes para os métodos da classe Calculadora
    # -----------------------------------------------------
    def setUp(self):
        """Instancia a classe antes de cada teste."""
        self.calc = Calculadora()

    def test_metodo_somar(self):
        self.assertEqual(self.calc.somar(10, 20), 30)
        self.assertEqual(self.calc.somar(-1, 1), 0)

    def test_metodo_dividir_valido(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertAlmostEqual(self.calc.dividir(5, 2), 2.5)

    # -----------------------------------------------------
    # Item 3: Validação de entradas inválidas (Exceção)
    # -----------------------------------------------------
    def test_divisao_por_zero_lanca_excecao(self):
        # Verifica se o método lança ValueError ao dividir por zero
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)


if __name__ == "__main__":
    unittest.main()