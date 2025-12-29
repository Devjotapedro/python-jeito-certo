# n = 10
# while n >= 0:
#     print(n)
#     n = n - 1
#     if n == 5:
#         break
    
#break encerra uma iteração
#continue pula uma repetição sem encerrar o loop

n = 10
while n >= 0:
    if n % 2 == 1:
        n = n - 1
        continue
    print(n)
    n = n - 1
    
#exercicio01 
#fatorial de um numero (while 5x4x3x2)
#exercicio02
#jogo de advinhar um número (se acertou ou se o chite é maior ou menor, até acertar )