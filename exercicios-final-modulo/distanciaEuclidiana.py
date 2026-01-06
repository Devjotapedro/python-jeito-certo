#Faça um programa que calcule a distância Euclidiana entre dois pontos do plano cartesiano.
import math

# ponto1 = int(input("Digite o ponto 1 do eixo x :"))
# ponto2 = int(input("Digite o ponto 2 do eixo x :"))
# ponto3 = int(input("Digite o ponto 1 do eixo y :"))
# ponto4 = int(input("Digite o ponto 2 do eixo y :"))

# distancia = math.sqrt(math.pow(ponto2 - ponto1, 2) + math.pow(ponto4 - ponto3, 2))
# print(f"A distância é de {distancia}")

eixoX = (1,4)
eixoy = (2,6)

distancia = math.sqrt((eixoX[1] - eixoX[0])**2 + (eixoy[1] - eixoy[0])**2)
print(f"A distância é de {distancia}")