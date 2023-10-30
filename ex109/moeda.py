def dobro(n, format=False):
    dob = n*2
    if format:
        print(f'>> O dobro de R${n:.2f} é R${dob:.2f}'.replace('.',','))

def metade(n, format=False):
    met = n/2
    if format:
        print(f'>> A metade de R${n:.2f} é R${met:.2f}'.replace('.',','))

def aumentar(n, format=False):
    aum = n*1.1
    if format:
        print(f'>> R${n:.2f} acrescido de 10% é R${aum:.2f}'.replace('.',','))

def diminuir(n, format=False):
    dim = n*0.9
    if format:
        print(f'>> R${n:.2f} reduzido em 10% é R${dim:.2f}'.replace('.',','))