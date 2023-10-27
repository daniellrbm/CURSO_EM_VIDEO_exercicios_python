#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
print('===== DESAFIO 101 =====')
# ÁREA DE FUNÇÕES
def voto(x):
    # biblioteca importada dentro da função para ser executada apenas em escopo local e economia de memória
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        print('~~' * 18)
        print(f'Você tem {idade} anos. Voto NEGADO.')
    elif idade >= 18 and idade <= 65:
        print('~~' * 18)
        print(f'Você tem {idade} anos. Voto OBRIGATÓRIO.')
    else:
        print('~~' * 18)
        print(f'Você tem {idade} anos. Voto OPCIONAL.')



# PROGRAMA PRINCIPAL
ano = int(input('Em que ano você nasceu? '))
voto(ano)