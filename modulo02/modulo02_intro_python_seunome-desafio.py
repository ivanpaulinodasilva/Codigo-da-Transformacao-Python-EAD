from datetime import datetime

nome = input("Por favor, digite o seu nome: ")

agora = datetime.now()
hora_formatada = agora.strftime("%H:%M")

print(f"Olá, {nome}! Agora são {hora_formatada}. Tenha um excelente momento de estudos!")