print("===== DESAFIO 93 =====")
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# GERANDO UM NOVO DICIONÁRIO:
dados_jogador = dict()

# INCLUIDO OS PRIMEIROS DADOS NO DICIONÁRIO:
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

# IMPRIMIDO OS RESULTADOS
print("=-" * 20)
print(f'NOME DO JOGADOR: {dados_jogador["nome"]}\n'
      f'PARTIDAS JOGADAS: {dados_jogador["jogos"]}')

for index, gol in enumerate(gols):
    print(f'>>> Na {index + 1}a partida marcou {gol} gol(s)')

print(f'GOLS MARCADOS: {dados_jogador["total_gols"]}\n'
      f'APROVEITAMENTO: {dados_jogador["aproveitamento"]:.2f}%')