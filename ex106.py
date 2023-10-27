# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
print('===== DESAFIO 106 =====')
cores = ['\033[m',        # 0. texto normal
         '\033[0;30;42m', # 1. fundo verde
         '\033[0;30;44m', # 2. fundo azul
         '\033[0;30;41m', # 3. fundo vermelho
         '\033[7m'        # 4. fundo branco
         ]

def cabecalho(txt, cor=0):
    tam = len(txt)+2
    print(cores[cor], end="")
    print('=' * tam)
    print(txt, cores[1])
    print('=' * tam)
    print(cores[0], end="")

def mensagem(msg, cor=0):
    print(cores[cor], end="")
    print(msg)
    print(cores[0], end="")
def pyhelp(cmd):
    while True:
        if cmd.upper().strip() == 'FIM':
            mensagem('Encerrando o programa. Até Logo!', 3)
            break
        else:
            mensagem(f'Você abriu a documentação de {cmd}', 2)
            print(cores[4], end="")
            help(cmd)
            print(cores[0], end="")
            cabecalho(' SISTEMA DE AJUDA PyHELP', 1)
            cmd = str(input('\033[mBiblioteca ou Função: '))



# PROGRAMA PRINCIPAL
cabecalho(' SISTEMA DE AJUDA PyHELP', 1)
comando = str(input('Biblioteca ou Função: '))
pyhelp(comando)