# Dada uma string com uma única letra e uma outra string qualquer, responda quantas vezes a letra está presente na outra string

while True:
    palavra1 = input("Digite uma palavra: ")
    letra1 = input("Digite uma letra: ")
    contador = 0
    for p in range(len(palavra1)):
        if letra1.lower() in palavra1[p].lower():
            contador += 1
    print(f"A letra {letra1} aparece {contador} vezes em {palavra1}")
    per = input("Deseja outra palavra? (sim/não)")
    if per != "sim":
        print(f"-------- Encerrando ---------")
        break
    