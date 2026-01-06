# Ainda considerando uma string com uma única letra e uma outra string qualquer, responda com uma lista de índices indicando as posições em que a letra está presente.

while True:
    posicao = []
    palavra1 = input("Digite uma palavra: ")
    letra1 = input("Digite uma letra: ")
    for p in range(len(palavra1)):
        if letra1.lower() in palavra1[p].lower():
            posicao.append(p)
    print(f"A letra {letra1} aparece nos indices {posicao} em {palavra1}")
    per = input("Deseja outra palavra? (sim/não)")
    if per != "sim":
        print(f"-------- Encerrando ---------")
        break
    