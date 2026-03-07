import random

DISCIPLINAS = [
    'Língua Portuguesa',
    'Matemática',
    'Física',
    'Química',
    'Biologia',
    'Língua Inglesa',
    'Geografia',
    'História'
]

BIMESTRES = 4


def gerar_notas():
    notas = []
    for _ in range(BIMESTRES):
        notas.append(random.randint(0, 10))
    return notas


def calcular_media(notas):
    return sum(notas) / len(notas)


def definir_situacao(media):
    if media >= 6:
        return "Aprovado"
    elif media > 4:
        return "Recuperação"
    else:
        return "Reprovado"


with open("notas2.txt", "w", encoding="utf-8") as arquivo:

    for disciplina in DISCIPLINAS:

        notas = gerar_notas()
        media = calcular_media(notas)
        situacao = definir_situacao(media)

        arquivo.write(f"Disciplina: {disciplina}\n")

        for i, nota in enumerate(notas, start=1):
            arquivo.write(f"Bimestre {i}: {nota}\n")

        arquivo.write(f"Média: {media:.2f}\n")
        arquivo.write(f"Situação: {situacao}\n")
        arquivo.write("-" * 40 + "\n")