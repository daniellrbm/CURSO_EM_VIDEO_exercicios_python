print('===== DESAFIO 82 =====')
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

listaNum = []
numPar = []
numImpar = []

while True:
    # DIGITANDO UM NOVO VALOR E INCLUINDO DENTRO DA LISTA....
    num = int(input('Digite um valor: '))
    listaNum.append(num)
    # MSEPARANDO OS ITENS EM LISTAS DE PARES E ÍMPARES...
    if num % 2 == 0:
        numPar.append(num)
    else:
        numImpar.append(num)
    perg = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    print('-' * 50)
    while perg not in 'SN':
        perg = str(input('OPÇÃO INVÁLIDA. Deseja Continuar? [S/N]: ')).strip().upper()[0]
        print('-' * 50)
    if perg == 'N':
        print('=' * 50)
        break

# IMPRIMINDO AS INFORMAÇÕES PEDIDAS NO EXERCÍCIO...
print(f'>> Os valores digitados foram {listaNum}')
print(f'>> Os valores PARES digitados foram {numPar}')
print(f'>> Os valores ÍMPARES digitados foram {numImpar}')
