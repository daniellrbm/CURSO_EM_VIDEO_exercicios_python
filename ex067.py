print('===== DESAFIO 67 =====')
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('=' * 40)
    if num <= 0:
        break
    for tab in range(1, 11):
        print(f'{num} x {tab} = {num * tab}')
    print('=' * 40)
print('VOCÊ DIGITOU ZERO OU UM VALOR NEGATIVO.\nFIM DO PROGRAMA.')

