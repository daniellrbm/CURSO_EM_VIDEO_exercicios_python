# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
print('===== DESAFIO 103 =====')

def ficha(a='<DESCONHECIDO>',b='<VALOR INVÁLIDO>'):
    print('=-' * 25)
    print(f'O jogador {a.upper()} marcou {b} gol(s) no campeonato.')

# PROGRAMA PRINCIPAL
jogador = str(input('NOME DO JOGADOR: '))
gols = str(input('GOLS MARCADOS: '))
# se a string digitada em gols for um número, converte-se a string num inteiro
if gols.isnumeric():
    int(gols)
# se a string com o nome do jogador estiver vazia...
if jogador.strip() == "":
    ficha(b=gols) # exibe o parametro opcional da função + numero de gols digitado
else:
    ficha(a=jogador) # exibe o nome do jogador digitado

#ficha(jogador, gols)