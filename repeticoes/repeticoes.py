alunos = ("JP", "Maria", "Jose", "Ana")

#iterações definidas
for aluno in alunos:
    print(aluno)
    print("-----")
print("Acabaram os nomes")

#0 a 9
for numero in range(10):
    print(numero)
    
#3 a 9, incrementando 2
for numero in range(3, 10, 2):
    print(numero)


for idx in range(len(alunos)):
    print(alunos[idx])