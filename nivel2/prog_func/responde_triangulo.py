from triangulos import triangulo_valido

#pensar em funções que retornam valores e deixar a parte da exibição a cargo do programa que utiliza a função

a = float(input("Digite um valor de lado: "))
b = float(input("Digite um valor de lado: "))
c = float(input("Digite um valor de lado: "))

if triangulo_valido(a,b,c):
    print(f"{a}, {b}, e {c} formam um triângulo válido")
else:
    print(f"{a}, {b}, e {c} não formam um triângulo válido")