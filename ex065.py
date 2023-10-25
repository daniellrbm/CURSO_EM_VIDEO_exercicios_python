print('===== DESAFIO 65 =====')
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# TODAS ESTAS 4 VARIÁVEIS TERÃO O PRIMEIRO VALOR DE N COMO PONTO DE PARTIDA...
n = soma = maior = menor = int(input('Digite um número: '))
sOUn = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = 0
c = 1

while sOUn == 'S':
    n = int(input('Digite um novo número: '))
    if n > maior: # DETERMINANDO O MAIOR VALOR...
        maior = n
    elif n < menor: # DETERMINANDO O MENOR VALOR...
        menor = n
    c += 1
    soma += n
    media = soma / c
    sOUn = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
print('=' * 40)
# PRINTANDO OS RESULTADOS...
print('>>> Foram digitados {} valores.'.format(c))
print('>>> O MAIOR valor digitado foi {}.'.format(maior))
print('>>> O MENOR valor digitado foi {}.'.format(menor))
print('>>> A SOMA dos valores digitados é {}.'.format(soma))
print('>>> A MÉDIA dos valores digitados é {:.1f}.'.format(media))
