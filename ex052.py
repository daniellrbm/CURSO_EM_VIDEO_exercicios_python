print('===== DESAFIO 52 =====')
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))

if num % 2 == 0 or num % 3 == 0:
    print('{} não um número primo.'.format(num))
else:
    print('{} é um número primo.'.format(num))