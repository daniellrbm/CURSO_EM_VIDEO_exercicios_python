print('=====  DESAFIO 71 =====')
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valorSaque = int(input('Qual valor deseja sacar? R$ '))
total = valorSaque
print('=' * 40)
print(f'PARA SACAR R${valorSaque:.2f}')
MaiorNota = 100 # VALOR DA MAIOR NOTA DISPONÍVEL...
totNotas = 0

while True:
    # ENQUANTO O VALOR DO SAQUE FOR MAIOR QUE O VALOR DA MAIOR NOTA DISPONÍVEL, O VALOR DESTA NOTA SERÁ SUBTRAÍDO DO TOTAL...
    if total >= MaiorNota:
        total -= MaiorNota
        totNotas += 1
    else: # QUANDO NÃO FOR MAIS...
        if totNotas > 0:
            print(f'>> {totNotas} notas de R${MaiorNota}')
        if MaiorNota == 100:
            MaiorNota = 50 # O MAIOR VALOR PASSA DE 100 PARA 50...
        elif MaiorNota == 50:
            MaiorNota = 20 # O MAIOR VALOR PASSA DE 50 PARA 20...
        elif MaiorNota == 20:
            MaiorNota = 10 # O MAIOR VALOR PASSA DE 20 PARA 10..
        elif MaiorNota == 10:
            MaiorNota = 5 # O MAIOR VALOR PASSA DE 10 PARA 5..
        elif MaiorNota == 5:
            MaiorNota = 2 # O MAIOR VALOR PASSA DE 5 PARA 2..
        elif MaiorNota == 2:
            MaiorNota = 1 # O MAIOR VALOR PASSA DE 2 PARA 1..
        totNotas = 0

        if total == 0: # QUANDO O VALOR DO SAQUE ZERAR...
            break
print('=' * 40)