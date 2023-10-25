print("===== DESAFIO 92 =====")
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

# GERANDO O DICIONARIO QUE TERÁ OS DADOS DO TRABALHADOR
dados = {}

# INSERINDO OS DADOS DO TRABALHADOR:
dados['nome'] = str(input("Nome do Trabalhador: "))
ano_nasc = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - ano_nasc
dados['CTPS'] = int(input("Número da CTPS (0 = Não tem): "))

if dados['CTPS'] != 0:
    dados['ano_contratacao'] = int(input("Ano de Contratação: "))
    dados['salario'] = float(input("Salário: R$ "))
    dados['idade_aposentadoria'] = (dados['ano_contratacao'] + 35) - ano_nasc

print("=-" * 30)
for key, value in dados.items():
    print(f'>> {key} tem o valor {value}')


