print('===== DESAFIO 55 =====')
#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Insira o peso da {}a pessoa (Kg): '.format(c)))
    if c == 1:
        #no primeiro laço o valor digitado será o maior e o menor peso a fim de comparação com os demais valores a serem registrados
        maior = peso
        menor = peso
    else:
        #se os valores seguintes forem maiores que seus anteriores no laço...
        if peso > maior:
            maior = peso
        # se os valores seguintes forem menores que seus anteriores no laço...
        if peso < menor:
            menor = peso
print('='*40)
print('O maior peso registrado foi {:.1f} Kg.\n'
      'O menor peso registrado foi {:.1f} Kg.'.format(maior, menor))