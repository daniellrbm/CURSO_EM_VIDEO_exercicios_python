print('===== DESAFIO 66 =====')
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = soma = count = 0

while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    count += 1
    soma += n
print('=' * 40)
print(f'>> Foram digitados {count} números.')
print(f'>> A soma dos números digitados é {soma}.')