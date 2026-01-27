#exercicio: programa com função que recebe 3 valores numericos e diz se dá pra formar um triângulo  ou não


def formar_triangulo(n1, n2, n3):
    if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
        return "Dá para formar um triângulo"
    else:
        return "Não forma"
    
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

print(formar_triangulo(n1, n2, n3))