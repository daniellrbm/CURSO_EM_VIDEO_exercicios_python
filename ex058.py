print('===== DESAFIO 58 =====')
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print(str('OI, EU SOU SEU COMPUTADOR.\n'
          'EU PENSEI EM UM NÚMERO ENTRE 0 E 10.\n'
          'SERÁ QUE VOCÊ CONSEGUE ADIVINHAR QUAL?'))
print('=-' * 20)

numPC = randint(0, 10)
palpite = int(input('Qual o seu palpite? '))
totPalpite = 1

# ENQUANTO O PALPITE NÃO ESTIVER CERTO...
while palpite != numPC:
    totPalpite += 1
    if palpite < numPC: # SE O PALPITE FOR MAIOR QUE O NUMERO DO PC
        palpite = int(input('Um pouco mais... Tente de novo: '))
    else: # SE O PALPITE FOR MENOR QUE O NUMERO DO PC
        palpite = int(input('Um pouco menos... Tente de novo: '))

# SE O PALPITE ESTIVER CERTO...
if totPalpite == 1: # ACERTANDO DE PRIMEIRA...
    print('=*' * 20)
    print('PARABÉNS! VOCÊ ACERTOU DE PRIMEIRA!')
else: # ACERTANDO COM MAIS CHANCES...
    print('=*' * 20)
    print('ACERTOU! VOCÊ PRECISOU DE {} PALPITES PARA ACERTAR.'.format(totPalpite))