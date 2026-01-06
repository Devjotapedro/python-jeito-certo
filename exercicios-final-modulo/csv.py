# Faça um programa que escreva um arquivo CSV* (valores separados por vírgulas), que armazene os nomes de alunos de uma escola e as suas notas em diversas disciplinas.

with open("aluno.csv", "w") as arquivo:
    # cabeçalho do arquivo
    arquivo.write("Nome, Matemática, fisica, história\n")
    
    while True:
        nome = input("Nome do aluno: ")
        nota_matematica = float(input("Digite a nota de Matemática: "))
        nota_fisica = float(input("Digite a nota de fisica: "))
        nota_historia = float(input("Digite a nota de história: "))
        
        #a linha do csv
        linha = f"{nome}, {nota_matematica}, {nota_fisica}, {nota_historia}\n"
        arquivo.write(linha)
        
        continuar = input("Deseja cadastrar outro aluno (s/n): ")
        if continuar.lower() != 's':
            break