#capturar vetores
#função para as operações

  
def capturar_vetores():

    #vetores
    vetor1 = []
    vetor2 = []
    
    for i in range(1,3):
        coordenada = float(input(f'Digite a coordenada {i} do primeiro vetor: '))
        vetor1.append(coordenada)
    
    for i in range(1,3):
        coordenada = float(input(f'Digite a coordenada {i} do segundo vetor: '))
        vetor2.append(coordenada)
    
    print(f'Vetor 1: {vetor1}, vetor 2: {vetor2}')
    return vetor1, vetor2
    

#somar vetores

def soma_vetores(v1, v2):
    vr = [
        v1[0] + v2[0],
        v1[1] + v2[1]
    ]
    
    print(f'O vetor resultante da soma é: {vr}')
    return vr
    

#subtrair vetores


def subtrai_vetores(v1, v2):
    vr = [
        v1[0] - v2[0],
        v1[1] - v2[1]
    ]
    
    print(f'O vetor resultante da subtração é: {vr}')
    return vr

#multiplicar vetores por numero

def multiplica_escalar(v1):
    n = float(input("Digite o valor de n: "))
    vr = [
        v1[0] * n,
        v1[1] * n
    ]
    print(f'O vetor resultante da multiplicação é: {vr}')
    return vr

#produto de2 vetores


def produto_escalar(v1, v2):
    produto = ((v1[0] * v2[0]) + (v1[1] * v2[1]))
    
    print(f'O produto é: {produto}')
    return produto

# vetor1, vetor2 = capturar_vetores()
# soma_vetores(vetor1, vetor2)
# subtrai_vetores(vetor1, vetor2)
# multiplica_escalar(vetor1)
# produto_escalar(vetor1, vetor2)

