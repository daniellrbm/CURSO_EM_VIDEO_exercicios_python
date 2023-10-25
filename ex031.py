print('=====  DESAFIO 31 =====')
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print('QUAL O PREÇO DA PASSAGEM???')

dist = float(input('Qual a distância que irá viajar? '))

if dist <= 200:
    precoPassagem = dist * 0.5
else:
    precoPassagem = dist * 0.45

print('Sua passagem custará R$ {:.2f}.'.format(precoPassagem))
print('Boa viagem!')