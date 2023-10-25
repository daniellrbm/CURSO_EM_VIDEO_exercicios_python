print('===== DESAFIO 88 =====')
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

lista = []

print('>>> GERADOR DE JOGOS DA MEGA SENA <<<')
qtd = int(input('Quantos jogos deseja gerar? '))

for jogos in range(0, qtd):
    # GERANDO UMA SUBLISTA DENTRO DA LISTA ORIGINAL...
    lista.append([])
    for num in range(0, 6):
        # 6 NUMEROS ALEATÓRIOS SERÃO ADIOCIONADOS NA SUBLISTA RECÉM GERADA...
        lista[jogos].append(randint(1, 60))

print('=' * 40)
# IMPRIMINDO OS JOGOS GERADOS...
for j in range(0, qtd):
    lista[j].sort()
    print(f'>> Jogo #{j + 1}: {lista[j]}')
    sleep(0.5)

print('BOA SORTE!')