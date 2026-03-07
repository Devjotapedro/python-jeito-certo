#gerar 4 notas para cada matéria
#colocar esses dados em um arquivo

import random

notas = []

disciplinas = ['Lingua portuguesa', 'Matemática', 'Física', 'Quimica', 'Biologia', 'Lingua inglesa', 'Geografia', 'História']

for disciplina in disciplinas:
    note = []
    for i in range(4):
        nota = random.randint(0,10)
        note.append(nota)
        boletim = f'Bimestre: {i + 1} | Disciplina: {disciplina} | Nota: {nota} |\n'
        #print(boletim)
        with open("notas.txt", "a") as list:
            list.writelines(boletim)
    #print(note)
    media =sum(note)/4
    #print(media)
    situacao = ''
    if media >= 6:
        situacao = 'Aprovado'
    elif media < 6 and media > 4:
        situacao = 'Recuperação'
    else:
        situacao = 'Reprovado'
    #print(boletim)
    resultado = (f'Média: {media} | Situação: {situacao} | \n')
    with open("notas.txt", 'a') as arq:
        arq.writelines(resultado)
    
    #print(f'Média: {media} | Situação: {situacao}')
    #com append colocar os outros dados
    
        