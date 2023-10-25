print('===== DESAFIO 23 =====')
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número: '))
und = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print('Analisando o número {}...\n'
      'Unidade(s): {};\n'
      'Dezena(s): {};\n'
      'Centena(s): {};\n'
      'Milhar(es): {}'.format(num, und, dez, cen, mil))