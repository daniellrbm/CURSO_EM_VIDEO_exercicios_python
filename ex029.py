print('===== DESAFIO 29 =====')
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Qual a velocidade do veículo? '))
multa = (vel - 80) * 7

if vel > 80:
    print('Você será multado por exceder o limite da via (80 km/h).\n'
          'Sua multa será no valor de R$ {:.2f}.'.format(multa))
else:
    print('Velocidade dentro so limite da via. Parabéns.')