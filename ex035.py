print('=====  DESAFIO 35 =====')
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('UM TRIÂNGULO É POSSÍVEL???')
r1 = int(input('Digite a medida da 1a reta: '))
r2 = int(input('Digite a medida da 2a reta: '))
r3 = int(input('Digite a medida da 3a reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível criar um triângulo com estes valores.')
else:
    print('Não é possível criar um triângulo com estes valores.')
