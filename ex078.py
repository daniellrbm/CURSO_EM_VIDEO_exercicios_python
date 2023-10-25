print('===== DESAFIO 78 =====')
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = menor = 0
listaNum = []

for c in range(0, 5):
    listaNum.append(int(input(f'Digite o {c + 1}o valor: ')))

    # DEFININDO O MAIOR E MENOR VALOR DIGITADO NA LISTA....
    if c == 0:
        maior = menor = listaNum[c]
    elif listaNum[c] > maior:
        maior = listaNum[c]
    elif listaNum[c] < menor:
        menor = listaNum[c]


print('=' * 40)
print(f'>> A lista que você digitou: {listaNum}')
print(f'>> O MAIOR valor digitado foi {maior}, na posição ', end='')
# ENCONTRANDO A/AS POSIÇÕES DO MAIOR VALOR
for i, v in enumerate(listaNum):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\n>> O MENOR valor digitado foi {menor}, na posição ', end='')
# ENCONTRANDO A/AS POSIÇÕES DO MENOR VALOR
for i, v in enumerate(listaNum):
    if v == menor:
        print(f'{i}... ', end='')
