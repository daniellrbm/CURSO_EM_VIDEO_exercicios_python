def dobro(n, format=False):
    dob = n*2
    if format:
        print(f'>> O dobro de R${n:.2f}: \tR${dob:.2f}'.replace('.',','))

def metade(n, format=False):
    met = n/2
    if format:
        print(f'>> A metade de R${n:.2f}:\tR${met:.2f}'.replace('.',','))

def aumentar(n, tx, format=False):
    # Inclusão de parâmetro tx (taxa) para cálculo de porcentagens variadas...
    aum = n + (n*tx)/100
    if format:
        print(f'>> Com acréscimo de {tx}%: \tR${aum:.2f}'.replace('.',','))

def diminuir(n, desc, format=False):
    # Inclusão de parâmetro desc (desconto) para cálculo de porcentagens variadas...
    dim = n - (n*desc)/100
    if format:
        print(f'>> Com desconto de {desc}%: \tR${dim:.2f}'.replace('.',','))

def resumo(n, tx, desc):
    print('=-' * 20)
    print('RESUMO DOS VALORES'.center(40))
    print('=-' * 20)
    # dobro e metade só precisam do parâmetro de preço...
    dobro(n, True)
    metade(n, True)
    # aumentar precisará de preço e taxa...
    aumentar(n, tx, True)
    # diminuir precisará de preço e desconto...
    diminuir(n, desc, True)
    print('=-' * 20)