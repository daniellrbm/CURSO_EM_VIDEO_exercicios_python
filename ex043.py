print('===== DESAFIO 43 =====')
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status

altura = float(input('Digite a sua altura (m): '))
peso = float(input('Digite o seu peso (Kg): '))
imc = peso / (altura ** 2) #ou pow(altura, 2) ou (altura * altura)

if imc > 40:
    print('\nIMC: {:.1f} >> OBESIDADE MÓRBIDA'.format(imc))
elif imc > 30 and imc <=40:
    print('\nIMC: {:.1f} >> OBESIDADE'.format(imc))
elif imc > 25 and imc <= 30:
    print('\nIMC: {:.1f} >> SOBREPESO'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('\nIMC: {:.1f} >> PESO IDEAL'.format(imc))
else:
    print('\nIMC: {:.1f} >> ABAIXO DO PESO'.format(imc))