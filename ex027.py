print('===== DESAFIO 27 =====')
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().upper()
nomeLista = nome.split()
pNome = nomeLista[0]
uNome = nomeLista[-1] # -1 se refere ao último item da lista

print('Analisando seu nome...\n'
      'Seu primeiro nome é {};\n'
      'Seu último nome é {}.'.format(pNome, uNome))
