alunos = ["Pedro", "Lara"]
notas = []



for nome in alunos:
    with open (f"python-jeito-certo/live1/notas/{nome.lower()}.csv", 'r') as arq:
        linhas = arq.readlines()
    for linha in linhas:
        partes = linha.strip().split(',')
        partes = [nome] + partes
        notas.append(tuple(partes))
print(notas)

with open("python-jeito-certo/live1/notas/resultado.csv", 'w') as arq:
    arq.write("Nome, Disciplina, Nota\n")
    for linha in notas:
        arq.write(f"{linha[0]}, {linha[1]}, {linha[2]}\n")
print("FINALIZOU COM SUCESSO!")