#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
print('===== DESAFIO 102 =====')
# AREA DE FUNÇÕES
def fatorial(num, show=False):
    fat = 1
    for cont in range(num, 0, -1):
        # Se o show for determinado como True...
        if show:
            if cont > 1:
                print(f'{cont} x', end=" ")
            else:
                print(f'{cont} = ', end="")
        fat *= cont
    print(fat)


# PROGRAMA PRINCIPAL
numero = int(input('Qual número deseja fatorar? '))
 # mostrar apenas o resultado da fatoração
fatorial(numero)
# mostrar a conta e o resultado da fatoração
fatorial(numero, show=True)
