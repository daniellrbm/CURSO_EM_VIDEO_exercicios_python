print('===== DESAFIO 85 =====')
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)

print('=' * 40)
lista[0].sort()
print(f'>> Os valores PARES digitados foram {lista[0]}')
lista[1].sort()
print(f'>> Os valores ÍMPARES digitados foram {lista[1]}')