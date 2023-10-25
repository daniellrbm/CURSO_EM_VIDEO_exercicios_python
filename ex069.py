print('===== DESAFIO 69 =====')
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

over18 = 0
male = 0
femaleUnder18 = 0

while True:
    # PERGUNTANDO A IDADE DO USUÁRIO...
    idade = int(input('Qual a sua idade? '))
    if idade > 18:
        over18 += 1

    # PERGUNTANDO O SEXO DO USUÁRIO...
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo [M/F]? ')).strip().upper()[0]
    if sexo == 'M':
        male += 1
    if sexo == 'F' and idade < 18:
        femaleUnder18 += 1

    # PERGUNTANDO SE O USUÁRIO DESEJA CONTINUAR COM O CADSTRO...
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    print('=' * 40)

print('=' * 40)
print('RESULTADOS:')
print(f'>> Foram cadastradas {over18} pessoas maiores de 18 anos.')
print(f'>> Foram cadastradas {male} pessoas do sexo masculino.')
print(f'>> Foram cadastradas {femaleUnder18} pessoas do sexo feminino menores de 18 anos.')