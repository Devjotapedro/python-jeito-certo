nota = float(input("Digite um valor de nota: "))

while nota < 0 or nota > 10:
    nota = float(input("Digite um valor válido de nota: "))
print(nota)