caracter = "55.1"

#iterar sobre o numero
#procurar um ponto
#remover o ponto
#ver se é numero

ponto = "."

if ponto in caracter:
    print("tem um ponto")
    resultado = caracter.replace(".", "")
    print(resultado)
    print(resultado.isdigit())
else:
    print("Não tem um ponto")
    print(caracter.isdigit())
