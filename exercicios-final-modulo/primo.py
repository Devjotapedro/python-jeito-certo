#Implemente um programa que responde se um número é primo ou não. Você pode assumir que este número não será maior que 10000 (dez mil).

#pega um número
#divide ele pelos demais até chegar nele mesmo
#conta 1 sempre que o resta da divisão for 1
#se o contador for igual a 2 é pq o número é primo



while True:
    contador = 0
    numero = int(input("Digite um número menor 10000: "))
    if numero <= 1:
        print("Números menores ou iguais a 1 não são primos.")
        continue
    for n in range (1, numero + 1):
            if numero % n == 0:
                contador +=1
    if contador == 2:
        print(f"O número {numero} é primo")
    else:
        print(f"O número {numero} não é primo")
    res = input("Deseja perguntar outro número (sim/nao)? ")
    if res != "sim":
        print("-------- Saindo do programa ----------")
        break
        