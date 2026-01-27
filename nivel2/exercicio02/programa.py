import perimetro as p
from area import calc_area

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

def triangulo(a, b, c):
    if a <= 0 or b <= 0 or c<= 0:
        return False
    elif a > (b + c):
        return False
    elif b > (a + c):
        return False
    elif c > (a + b):
        return False
    else:
        return True

if triangulo(a,b,c):
    print('Perimetro: ', p.calc_perimetro(a,b,c))
    print(f'Área: {calc_area(a, b, c):.2f}')
else:
    print('Não forma um triangulo válido')