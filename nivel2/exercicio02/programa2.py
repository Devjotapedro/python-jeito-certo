import perimetro as p
from area import calc_area

with open('python-jeito-certo/nivel2/exercicio02/lados.txt') as arq:
    linhas = arq.readlines()
for linha in linhas:
    partes = linha.strip().split()
    for i in range(len(partes)):
        partes[i] = float(partes[i])
    
    if partes[0] <= 0 or partes[1] <= 0 or partes[2] <= 0:
        print('Não forma um triangulo')
    elif partes[0] > (partes[1] + partes[2]) or partes[1] > (partes[0] + partes[2]) or partes[2] > (partes[0] + partes[1]):
        print('Não forma um triâmgulo')
    else:
        
        perimetro = p.calc_perimetro(partes[0], partes[1], partes[2])
        area = calc_area(partes[0], partes[1], partes[2])

print(f'A área do triangulo é: {area:.2f}')
print(f'O perimetro do triangulo é: {perimetro}')
    
    