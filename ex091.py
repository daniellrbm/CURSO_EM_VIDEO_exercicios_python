print("===== DESAFIO 91 =====")
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

# CRIANDO O DICIONÁRIO COM OS 4 JOGADORES:
jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)}

# EXIBINDO OS VALORES TIRADOS PELOS JOGADORES NO DADO:
for key, value in jogo.items():
    print(f' O {key} tirou {value}')
    sleep(0.5)
print("=-" * 15)

# CRIANDO UM DICIONÁRIO PARA RANQUEAR OS RESULTADOS,
ranking = ()

# RANQUEANDO USANDO O ITEMGETTER EM ORDEM DECRESCENTE
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)     # com a insersão dos valores do ranking, este dicionário        passará a ser tratado como lista.

# EXIBINDO O RESULTADO DO JOGO:
print("RESULTADO:")
for index, value in enumerate(ranking):
    print(f'{index + 1}o LUGAR: {value[0]}, que tirou {value[1]}.')