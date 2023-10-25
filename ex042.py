print('===== DESAFIO 42 =====')

# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

print('UM TRIÂNGULO É POSSÍVEL??? E QUAL?')
r1 = int(input('Digite a medida da 1a reta: '))
r2 = int(input('Digite a medida da 2a reta: '))
r3 = int(input('Digite a medida da 3a reta: '))

# ANALISANDO SE SERÁ POSSÍVEL FORMAR UM TRIANGULO COM AS MEDIDAS
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nÉ possível criar um triângulo com estes valores.')

    # DEFININDO QUE TIPO DE TRIANGULO SERÁ FORMADO
    if r1 == r2 and r2 == r3:
        print('Este será um triângulo EQUILÁTERO.')
    elif r1 != r2 and r2 != r3:
        print('Este será um triângulo ESCALENO.')
    else:
        print('Este será um triângulo ISÓSCELES.')

else:
    print('\nNão é possível criar um triângulo com estes valores.')

