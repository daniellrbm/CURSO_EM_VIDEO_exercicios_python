print('===== DESAFIO 96 =====')
#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg} x {comp} é de {a:.2f}m².')

# PROGRAMA PRINCIPAL...
print()
print('CÁLCULO DE ÁREA DE TERRENOS')
print('=-' * 20)
lrg = float(input('LARGURA (m): '))
cmp = float(input('COMPRIMENTO (m): '))
area(lrg, cmp)
