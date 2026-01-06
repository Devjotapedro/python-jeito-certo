# Faça um programa que leia um arquivo de texto em que cada linha tem dois números separados por espaço em branco. Para cada linha, some os números e salve os resultados em um outro arquivo de texto (cada linha deve conter o resultado da soma da linha correspondente).

#criar um arquivo com 2 números por linha
#somar os numeros de cada linha
#em outro arquivo exibir o resultado da soma em cada linha

#tirar espaços
#transforma em numeros
#somar

caminho = '/home/jp/dev/estudo/python-do-jeito-certo/python-jeito-certo/exercicios-final-modulo/numeros.txt'


with open(caminho, 'r') as arq:
    conteudo = arq.read()
    #separar por linhas
    linhas = conteudo.splitlines()
    #percorrente cada linha
    for linha in linhas:
        #parte o numero em 2
        numeros = linha.split()
        n1 = int(numeros[0])
        n2 = int(numeros[1])
        soma = n1 + n2
        print(soma)



with open('resultado.txt', 'w') as saida:
    for linha in linhas:
        n1, n2 = linha.split()
        saida.write(str(int(n1) + int(n2)) + '\n')

