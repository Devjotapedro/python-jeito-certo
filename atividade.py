# array recebido
numeros = [1, 2, 3, 4, 5]

# índices do início e do final
inicio = 0
fim = len(numeros) - 1

# inverter os elementos
while inicio < fim:
    temp = numeros[inicio]
    numeros[inicio] = numeros[fim]
    numeros[fim] = temp

    inicio += 1
    fim -= 1

# saída
print(numeros)