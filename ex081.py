print('===== DESAFIO 81 =====')
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

listaNum = []

while True:
    # DIGITANDO UM NOVO VALOR E INCLUINDO DENTRO DA LISTA....
    num = int(input('Digite um valor: '))
    listaNum.append(num)
    perg = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    print('-' * 50)
    while perg not in 'SN':
        perg = str(input('OPÇÃO INVÁLIDA. Deseja Continuar? [S/N]: ')).strip().upper()[0]
        print('-' * 50)
    if perg == 'N':
        print('=' * 50)
        break

# IMPRIMINDO AS INFORMAÇÕES PEDIDAS NO EXERCÍCIO...
listaNum.sort(reverse=True) # COLOCARNDO OS ITENS DA LISTA EM ORDEM DECRESCENTE
print(f'>> A lista criada em order DECRESCENTE foi {listaNum}')
print(f'>> A lista criada contém {len(listaNum)} valores')
if 5 in listaNum:  # VERIFICANDO SE O NUMERO 5 FAZ PARTE DA LISTA...
    print('>> O número 5 está contido na lista criada!')
else:
    print('>> O número 5 não está contido na lista criada.')