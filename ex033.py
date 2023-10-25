print('===== DESAFIO 33 =====')
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))

# testado o menor numero
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O menor número digitado é {}'.format(menor))

# testado o maior numero
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior número digitado é {}'.format(maior))