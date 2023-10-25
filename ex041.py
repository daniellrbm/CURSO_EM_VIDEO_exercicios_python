from datetime import date

print('===== DESAFIO 41 =====')
#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

nasc = int(input('Atleta, digite seu ano de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('Com {} anos, sua categoria é MIRIM.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Com {} anos, sua categoria é INFANTIL.'.format(idade))
elif idade > 14 and idade <= 16:
    print('Com {} anos, sua categoria é JUVENIL.'.format(idade))
elif idade > 16 and idade <= 19:
    print('Com {} anos, sua categoria é JÚNIOR.'.format(idade))
elif idade > 19 and idade <= 25:
    print('Com {} anos, sua categoria é SÊNIOR.'.format(idade))
else:
    print('Com {} anos, sua categoria é MASTER.'.format(idade))

