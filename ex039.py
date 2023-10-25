from datetime import date

print('===== DESAFIO 39 =====')
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

nasc = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nasc

if idade < 18:
    print('Ainda não é hora de se alistar.\n'
          'Falta(m) {} ano(s) para o alistamento obrigatório.\n'
          'Seu alistamento será em {}.'.format(18 - idade, nasc + 18))
elif idade == 18:
    print('Você está na idade do Alistamento Militar.\n'
          'Apresente-se imediatamente!')
else:
    print('Você já deveria ter se alistado há {} ano(s).\n'
          'Seu alistamento foi em {}.'.format(idade - 18, nasc + 18))