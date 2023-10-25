print('===== DESAFIO 54 =====')
#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

under18 = 0
over18 = 0

for c in range(1,8):
    nasc = int(input('Informe o ano de nascimento da {}a pessoa: '.format(c)))
    idade = date.today().year - nasc
    if idade >= 18:
        over18 += 1
    else:
        under18 += 1
print('=' * 20)
print('Deste grupo de {} pessoas:\n'
      '>> {} pessoa(s) é/são maiores de idade;\n'
      '>> {} pessoa(s) é/são menores de idade;'.format(c, over18, under18))

