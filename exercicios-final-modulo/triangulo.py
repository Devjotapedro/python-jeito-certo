#Dados 3 valores numéricos não negativos, responda se é possível existir um triângulo cujas medidas sejam estes valores

valor1 = 4
valor2 = 7
valor3 = 12

if valor1 < valor2 + valor3 and valor2 < valor1 + valor3 and valor3 < valor1 + valor2:
    print("É possível existir um triângulo")
else:
    print("Não é possível existir um triângulo")