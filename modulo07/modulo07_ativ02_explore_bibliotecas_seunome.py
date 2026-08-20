'''
Programador: as variaveis, serão inseridas no app - BACK-End

Dev: existe a interação com o usuario - Web Design (Front-End)

'''
import utilidades
import datetime
from faker import Faker


fake = Faker('pt_BR')


print('***Dados Criados -  Prova de Matemática***')
print(f'Nome de Mentira: {fake.name()}')
print(f'E-Mail de Mentira: {fake.email()}')
print(f'Telefone de Mentira: {fake.phone_number()}')


print(f'Dados da Prova de Mentira ***')
agora = datetime.datetime.now()
print(f'Data e hora atual: {agora.strftime('%H:%M %d/%m/%Y')}')



num1 = 10
num2 = 5

print('⚙ 🧱Teste de Utilidades ⚙ 🧱')
print(f'Números utilizados: {num1} e {num2}')


print(f' Usando Adição ({num1} + {num2}) :', utilidades.soma(num1, num2))


print(f' Usando Subtrair ({num1} - {num2}) :', utilidades.subtrair(num1, num2))


print(f"Multiplicação ({num1} * {num2}):", utilidades.multiplicar(num1, num2))

print(f"Divisão ({num1} / {num2}):", utilidades.dividir(num1, num2))

print(f"Divisão Inteira ({num1} // {num2}):", utilidades.divisao_inteira(num1, num2))

print(f"Resto da Divisão ({num1} % {num2}):", utilidades.resto_divisao(num1, num2))

print(f"Potenciação ({num1} ^ {num2}):", utilidades.potencia(num1, num2))

print("\n=== TESTE DE SEGURANÇA (DIVISÃO POR ZERO) ===")
print("Divisão por zero:", utilidades.dividir(10, 0))