print('='*5 + ' DESAFIO 28 ' + '='*5)
#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

print('QUAL NÚMERO O PC VAI ESCOLHER?')
numPC = randint(0,5)
numPlayer = int(input('Digite um número entre 0 e 5: '))

if numPlayer == numPC:
    print('Você escolheu: {};\n'
          'O PC escolheu: {};\n'
          'VOCÊ VENCEU!'.format(numPlayer, numPC))
else:
    print('Você escolheu: {};\n'
          'O PC escolheu: {};\n'
          'NÃO FOI DESTA VEZ.'.format(numPlayer, numPC))