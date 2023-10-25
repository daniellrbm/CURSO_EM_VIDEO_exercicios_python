print('===== DESAFIO 63 =====')
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('SEQUÊNCIA DE FIBONACCI')
print('=-' * 30)
n = int(input('Quantos números da sequência de Fibonacci deseja visualizar? '))

a = 0
b = 1
count = 1

while count <= n:
    a = a + b # ATULIZANDO O VALOR DE A DE ACORDO COM O VALOR DE B...
    b = a - b # O NOVO VALOR DE B IRÁ ATUALIZAR O VALOR DE A NA CONTA ACIMA
    print('\033[1m{}\033[m'.format(a), end=' >> ')
    count += 1
print('\033[1mFIM\033[m')