print('=====  DESAFIO 48 =====')
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
tot = 0

for c in range (1, 501, 2):
    if c % 3 == 0:
        tot += 1
        s += c
print('Existem {} números múltiplos de 3 entre 1 e 500.\n'
      'A soma de todos estes números é {}'.format(tot, s))