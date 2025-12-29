n = int(input("Digite um número: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial = fatorial * i
print(f"fatorial de {n} é {fatorial} ")

fatorial = 1
p = n
while p > 0:
    fatorial = p * fatorial
    p -= 1
print(f"fatorial de {n} é {fatorial} ")