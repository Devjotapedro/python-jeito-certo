nota = input("Digite uma nota: ")
nota = float(nota)
media = float(input("Digite a média: "))

if nota >= media:
    print("Aprovado com nota", nota, "(media é", media, ")")
else:
    print(f"reprovado com a nota {nota} (média é {media})")
