print('===== DESAFIO 57 =====')
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

genero = str(input('Informe o seu gênero [M / F]? ')).strip().upper()

while genero != 'M' and genero != 'F':
    print('=-' * 20)
    genero = str(input('Opção Inválida. Informe o seu gênero [M / F]? ')).strip().upper()

print('=-' * 20)
if genero == 'M':
    print('Gênero MASCULINO registrado com sucesso!')
else:
    print('Gênero FEMININO registrado com sucesso!')