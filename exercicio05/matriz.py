#1 quantas linhas
#2 quantas colunas
#linhas e colunas não podem ser nulas e precisam ser numeros naturais
#matriz mxn

print("--------Escrevendo uma matriz --------")
linhas = int(input("Escreva a quantidade de linhas da matriz: "))
colunas = int(input("Escreva a quantidade de colunas da matriz: "))
if linhas > 0 and linhas != 0 and colunas > 0 and colunas != 0:
    print(f"Sua matriz terá {linhas} linhas e {colunas} colunas")
    matriz = [] 
    for i in range(1, linhas +1):
        linha = []
        print(f"valor de i = {i}")
        for j in range(1, colunas +1):
            print(f"valor de j = {j}")
            valores = int(input(f"Digite o valor na linha {i} coluna {j}: "))
            linha.append(valores)
        matriz.append(linha)
        print(f"matriz: {matriz}")
    print(matriz)
else:
    print("As linhas e colunas não podem ser 0 ou números negativos")

