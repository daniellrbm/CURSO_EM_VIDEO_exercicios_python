print('===== DESAFIO 60 =====')
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

# VERSÃO 01: USANDO A BIBLIOTECA MATH...
'''from math import factorial

num = int(input('Digite um número para saber o seu fatorial: '))
fat = factorial(num)

print('{}! = {}'.format(num, fat))'''

# VERSÃO 02: USANDO MÉTODOS TRADICIONAIS...
num = int(input('Digite um número para calcular o seu fatorial: '))
count = num
fat = 1

print('=-' * 20)
print('CALCULANDO {}! -> '.format(num), end='')
while count > 0:
    print('{}'.format(count), end=' ')
    print('x' if count > 1 else '=', end=' ')
    fat *= count
    count -= 1
print('\033[1:32m{}\033[m'.format(fat))