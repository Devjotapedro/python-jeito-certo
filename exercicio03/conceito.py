nota = float(input("Digite a nota: "))
if nota >= 9.0:
    conceito = "A"
elif nota >= 8.0:
    conceito = "B"
elif nota >= 7.0:
    conceito = "C"
elif nota >= 6.0:
    conceito = "D"
else:
    conceito = "F"
print(f"Conceito: {conceito}")