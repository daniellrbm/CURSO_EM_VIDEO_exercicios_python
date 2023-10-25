print('===== DESAFIO 40 =====')
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Digite a 1a nota: '))
n2 = float(input('Digite a 2a nota: '))
media = (n1 + n2) / 2

if media <= 5:
    print('Sua média: {:.1f}\n''Status: REPROVADO'.format(media))
elif media >= 7:
    print('Sua média: {:.1f}\n''Status: APROVADO'.format(media))
else:
    print('Sua média: {:.1f}\n''Status: EM RECUPERAÇÃO'.format(media))
