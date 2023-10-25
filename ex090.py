print("===== DESAFIO 90 =====")
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# GERANDO O DICIONÁRIO COM OS DADOS DO ALUNO
aluno = {}

# ADICIONANDO AS CHAVES NOME E MÉDIA AO DICIONÁRIO:
aluno["nome"] = str(input("Nome do aluno: "))
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))

# ADICIONANDO A CHAVE 'SITUAÇÃO' DE ACORDO COM A MÉDIA DO ALUNO:
if aluno['media'] >= 7:
    aluno["situacao"] = "APROVADO"
elif aluno['media'] <= 5:
    aluno["situacao"] = "REPROVADO"
else:
    aluno["situacao"] = "RECUPERAÇÃO"

# EXIBINDO OS RESULTADOS...
print("=-" * 20)
for key, value in aluno.items():
    print(f">> {key} do aluno é {value}.")
