print('===== DESAFIO 74 =====')
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

Tnum = (randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9))

print(f'VALORES SORTEADOS: {Tnum}')
print('=' * 40)
print(f'>> O maior valor sorteado foi {max(Tnum)}')
print(f'>> O menor valor sorteado foi {min(Tnum)}')