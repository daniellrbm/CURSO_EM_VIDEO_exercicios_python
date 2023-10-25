print('===== DESAFIO 56 =====')
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

mulherSub20 = 0
idadeHomemMaisVelho = 0
nomeHomemMaisVelho = ''
somaIdades = 0

for c in range(1, 5):
    # COLETANDO NOME, IDADE E GENERO DAS PESSOAS
    print('{}a PESSOA'.format(c))
    nome = str(input('Digite o seu nome: ')).strip().upper()
    idade = int(input('Sua idade: '))
    genero = str(input('Seu gênero (M/F): ')).strip().upper()
    print('=-' * 20)

    # FAZENDO A MEDIA DE IDADE DO GRUPO
    somaIdades += idade

    # REGISTRANDO O HOMEM MAIS VELHO
    if genero == 'M':
        if c == 1:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome
        elif idade > idadeHomemMaisVelho:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome

    # REGISTRANDO AS MULHERES COM MENOS DE 20 ANOS
    if genero == 'F' and idade < 20:
        mulherSub20 += 1

# IMPRIMINDO A MEDIA DE IDADE DO GRUPO
media = somaIdades / 4
print('A media de idade do grupo é de {:.1f} anos.'.format(media))

# IMPRIMINDO A IDADE DO HOMEM MAIS VELHO
print('>> O homem mais velho é {}, com {} anos.'.format(nomeHomemMaisVelho, idadeHomemMaisVelho))

# IMPRIMINDO RESULTADOS DAS MULHERES COM MENOS DE 20 ANOS
if mulherSub20 == 0:
    print('Nenhuma mulher tem menos de 20 anos.')
elif mulherSub20 == 1:
    print('Apenas 1 mulher tem menos de 20 anos.')
else:
    print('{} mulheres têm menos de 20 anos.'.format(mulherSub20))
