def triangulo_valido(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):
        return False
    return True

def perimetro(a, b, c):
    if triangulo_valido(a, b, c):
        return a + b + c
    return -1

def area(a, b, c):
    p = perimetro(a, b, c) / 2
    if p > 0:
        area = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
        return area
    return -1

def ler_vertices(filepath):
    #ler vertices d eum triangulo em um arquivo filepath
    with open(filepath) as arq:
        linhas = arq.readlines()
    vertices = []
    for linha in linhas:
        # partes = linha.split(",")
        # coordenadas = []
        # for parte in partes:
            #remove espaço na frente ou atrás
            # valor = float(parte.strip())
            # coordenadas.append(valor)
        coordenadas = [ float(c.strip()) for c in linha.split(",")]
        vertices.append(tuple(coordenadas))
    return vertices

def medir_lado(v1, v2):
    ndim = len(v1)
    diferencas = []
    for i in range(ndim):
        diferencas.append((v1[i] - v2[i]) ** 2)
    return sum(diferencas) ** (1/2)
    
def calcular_lados(triangulo):
    #retorna uma lista com o tamanho de cada lado do triângulo
    a = medir_lado(triangulo[0], triangulo[1])
    b = medir_lado(triangulo[1], triangulo[2])
    c = medir_lado(triangulo[2], triangulo[0])
    return(a, b, c)
    

#serve para dizer que esse é o módulo original e não o importado
if __name__ == "__main__":   
    vertices = ler_vertices("python-jeito-certo/nivel2/live2/data/vertices.txt")
    #print(vertices)
    
    #print(medir_lado((-1, -1), (0, 1)))
    print(calcular_lados(vertices))