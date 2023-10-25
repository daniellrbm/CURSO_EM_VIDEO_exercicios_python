print("=====DESAFIO 95 =====")
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

# GERANDO UM NOVO DICIONÁRIO:
dados_jogador = dict()
time = list()


# INCLUIDO OS PRIMEIROS DADOS NO DICIONÁRIO:
while True:
    dados_jogador['nome'] = str(input("Nome do Jogador: ")).capitalize()
    dados_jogador['jogos'] = int(input(f"Quantas partidas {dados_jogador['nome']} jogou? "))

    gols = list()
    total_gols = 0

    # ITERANDO QUANTOS GOLS O JOGADOR FEZ EM CADA PARTIDA
    for jogo in range(0, dados_jogador['jogos']):
        gol = int(input(f">> Quantos gols na {jogo + 1}a partida? "))
        gols.append(gol)
        total_gols += gol

    # INCLUINDO MAIS DADOS NO DICIONÁRIO APÓS ITERAÇÃO
    dados_jogador['gols_jogo'] = gols
    dados_jogador['total_gols'] = total_gols
    dados_jogador['aproveitamento'] = (total_gols * 100) / dados_jogador['jogos']

    # PERGUNTANDO SE DESEJA CADASTRAR MAIS JOGADORES...
    while True:
        resposta = str(input("Cadastrar outro jogador? [S?N] ")).upper()[0]

        if resposta in 'SN':
            print("--" * 20)
            break
        print('ERRO! Digitar S ou N.')
    if resposta == "N":
        break

# IMPRIMIDO OS RESULTADOS
print("=-" * 20)
for key, value in enumerate(time):
    print(f'{key:<3}', end=" ")
    for d in dados_jogador.values():
        print(f'{str(d):<15}', end=" ")