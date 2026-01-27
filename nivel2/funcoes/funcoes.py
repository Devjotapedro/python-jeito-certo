#funções são uma forma de nomear um conjunto especídico de instruções para realizar uma tarefa. 
#um bloco de código reutilizável

#n é parâmetro da função
def multiplicar_por_7(n):
    res = 7 * n
    return res

#10 é o argumento da função
r = multiplicar_por_7(10)
print("Resultado é", r)


def media_simples(a, b):
    return (a + b)/2
print(media_simples(10, 8))

def pedirInscricao():
    print("Inscreva-se")

pedirInscricao()

#exercicio: programa com função que recebe 3 valores numericos e diz se dá pra formar um triângulo  ou não