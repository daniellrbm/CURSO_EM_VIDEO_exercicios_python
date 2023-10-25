print('===== DESAFIO 34 =====')
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

print('CALCULANDO REAJUSTE SALARIAL')
sal = float(input('Digite o valor do seu salário atual: R$ '))

if sal >= 1250:
    reaj = sal * 1.1
    print('Você terá um reajuste de 10%.')
else:
    reaj = sal * 1.15
    print('Você terá um reajuste de 15%.')

print('Seu novo salário será de R$ {:.2f}'.format(reaj))
