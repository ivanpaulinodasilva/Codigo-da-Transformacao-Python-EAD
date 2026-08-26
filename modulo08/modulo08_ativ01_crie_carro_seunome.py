'''
class Carro:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# meu_carro = Carro("Chevrolet", "Camaro")
meu_carro = Carro("Renault", "Clio")
print(meu_carro.exibir_info())

'''

# Vai criar um bloco de comentario, sempre pelo menor valor. Minimo de uma Linha, não passar de Cinco.
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

print("🚗 CADASTRO DE VEÍCULO 🚗\n")

marca_digitada = input("Digite a marca do carro: ")
modelo_digitado = input("Digite o modelo do carro: ")

meu_carro = Carro(marca_digitada, modelo_digitado)

print("\n--- Informações do Carro Cadastrado ---")
print(meu_carro.exibir_info())