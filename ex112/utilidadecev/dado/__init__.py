def leiaDinheiro(txt):
    '''

    :param txt: Uma mensagem de texto a ser aplicada no programa principal, pedindo o usuário a inserir dados;
    :return: o dado inserido pelo usuário retornará uma string, que dará mensagem de erro se for alfanumérica. Caso contrário, a string será convertida em float e o programa seguirá rodando normalmente
    '''
    while True:
        # Entrada convertida numa string, trocando as vírgulas por pontos e retirando os espaços vazios...
        entrada = str(input(txt).replace(',', '.').strip())
        # Enquanto a entrada for alfanumérica ou vazia, dará mensagem de erro...
        if entrada.isalpha() or entrada =='':
            print(f'\033[0;31mERRO! "{entrada}" não é um valor válido.\033[m')
        # Caso contrário, a string será convertida em float e o programa seguirá rodando
        else:
            return float(entrada)
            break
