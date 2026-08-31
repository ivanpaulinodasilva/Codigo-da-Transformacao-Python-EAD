# ==============================================================================
# MÓDULO: aluno.py
# Descrição: Responsável por gerar dados do estudante usando Faker e Datetime.
# ==============================================================================

import datetime
from faker import Faker

# Inicialização do Faker no idioma português do Brasil
fake = Faker('pt_BR')

def gerar_aluno():
    """
    Gera dados cadastrais completos de um aluno fictício e calcula sua idade exata.
    Retorno: dict contendo nome, email, data de nascimento formatada e idade.
    """
    data_nasc = fake.date_of_birth(minimum_age=14, maximum_age=24)
    hoje = datetime.date.today()
    idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
    
    return {
        "nome": fake.name(),
        "email": fake.email(),
        "data_nascimento": data_nasc.strftime("%d/%m/%Y"),
        "idade": idade
    }