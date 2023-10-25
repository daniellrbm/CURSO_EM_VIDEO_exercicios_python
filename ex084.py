print('===== DESAFIO 84 =====')
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

lista = []
dados = []
maiorP = menorP = 0

while True:
    # INSERINDO DADOS NA LISTA PROVISÓRIA...
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(int(input('Peso(kg): ')))
    # REGISTRANDO O MAIOR E MENOR PESOS...
    if len(lista) == 0:
        maiorP = menorP = dados[1]
    else:
        if dados[1] > maiorP:
            maiorP = dados[1]
        if dados[1] < menorP:
            menorP = dados[1]
    # INSERIDO CÓPIA DOS DADOS CADASTRADOS NA LISTA PRINCIPAL...
    lista.append(dados[:])
    # LIMPANDO A LISTA DE DADOS PARA INSERIR NOVOS VALORES...
    dados.clear()

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-' * 40)

    if resp == 'N':
        break

print('=' * 40)
print(lista)
print(f'>> Total de pessoas cadastradas: {len(lista)}')
print(f'>> O MAIOR peso registrado: {maiorP}kg >>', end=' ')
# LAÇO PARA IDENTIFICAR OS NOMES DE MAIOR PESO...
for p in lista:
    if p[1] == maiorP:
        print(f'{p[0]}', end=' ')
print(f'\n>> O MENOR peso registrado: {menorP}kg >>', end=' ')
# LAÇO PARA IDENTIFICAR OS NOMES DE MENOR PESO...
for p in lista:
    if p[1] == menorP:
        print(f'{p[0]}', end=' ')