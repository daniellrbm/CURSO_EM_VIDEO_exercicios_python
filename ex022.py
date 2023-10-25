print('===== DESAFIO 22 =====')
#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas. // Quantas letras (sem considerar espaços) // Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

nomeSplit = nome.split() # quebrando o nome completo numa lista
pNome = len(nomeSplit[0]) # pegando o primeiro nome dessa lista
nomeStrip = nome.replace(" ", "") # removendo os espaços do nome
totLetras = len(nomeStrip)

print('Analisando seu nome...\n'
      'Em maiúsculas: {};\n'
      'Em minúsculas: {};\n'
      'Seu nome completo tem {} letras;\n'
      'Seu primeiro nome tem {} letras.'.format(nome.upper(), nome.lower(), totLetras, pNome))