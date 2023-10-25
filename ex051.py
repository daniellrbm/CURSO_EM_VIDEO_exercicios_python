print('===== DESAFIO 51 =====')
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

ptermo = int(input('Primeiro termo da PA: '))
razao = int(input('Progressão da PA: '))
dtermo = ptermo + (10 - 1) * razao

for c in range(ptermo, dtermo + razao, razao):
    print(c, end=' >> ')
print('Fim da PA')