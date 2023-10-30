def dobro(n: object) -> object:
    dob = n*2
    print(f'>> O dobro de R${n:.2f} é R${dob:.2f}')

def metade(n):
    met = n/2
    print(f'>> A metade de R${n:.2f} é R${met:.2f}')

def aumentar(n):
    aum = n*1.1
    print(f'>> R${n:.2f} acrescido de 10% é R${aum:.2f}')

def diminuir(n):
    dim = n*0.9
    print(f'>> R${n:.2f} reduzido em 10% é R${dim:.2f}')