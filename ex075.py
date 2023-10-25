print('===== DESAFIO 75 =====')
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

# ARMAZENANDO 4 VALORES NUMA TUPLA...
num = (int(input('Digite o 1º número: ')), int(input('Digite o 2º número: ')),
       int(input('Digite o 3º número: ')), int(input('Digite o 4º número: ')))


print('=' * 40)
print(f'Você digitou os numeros: {num}')
print('=' * 40)

# MOSTRANDO QUANTAS VEZES O NÚMERO 9 FOI DIGITADO NA TUPLA...
print(f'>> O número 9 foi digitado {num.count(9)} vezes.')

# MOSTRANDO A POSIÇÃO DO NÚMERO 3...
if 3 in num:
    print(f'>> O número 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print(f'>> O número 3 não foi digitado desta vez.')

# MOSTRANDO QUAIS NÚMEROS PARES FORAM DIGITADOS...
print(f'Os números pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(f'{c}, ', end='')