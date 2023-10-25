print('===== DESAFIO 64 =====')
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = int(input('Digite um número [999 para parar]: '))
soma = c = 0

# ENQUANTO O VALOR DE N NÃO FOR 999, OS VALORES DIGITADOS EM N SERÃO ADICIONADOS À SOMA...
while n != 999:
    soma += n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('A soma dos {} valores digitados [exceto 999] é {}.'.format(c, soma))
