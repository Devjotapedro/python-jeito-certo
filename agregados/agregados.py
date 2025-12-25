notas = [7.8, 8.2, 9.5]
disciplinas = ["matemática", "português", "filosofia"]
#print(notas, type(notas), type(notas[0]), notas[0])
print(f"A nota de {disciplinas[0]} foi {notas[0]}")
#listas são tipos de dados mutáveis

#adicionar elemento
disciplinas.append("história")
print(disciplinas[3])

#alterando valores
notas[0] = notas[0] + 1
print(notas[0])

#listas são agregados heterogenios, ou seja, posso adicionar tipos diferentes de dados
#são diferentes dos vetores (arrays) que são agregados homogêneos, ou seja, só posso adicionar um único tipo de dado

#posso acessar um dado negativo (contagem de trás para frente) -1 é o último dado

print(f"A nota de {disciplinas[-1]} foi {notas[-1]}")

#Tuplas são dados agregados imutáveis
#Também armanezam os valores de forma sequencial na memória e permite o acesso utilizando indices (iniciando no zero)
#Não é possivel adicionar novos elementos, nem modificar um valor

nomes = ("Maria", "João", "Paula")
print(nomes[0], nomes[-1])
#nomes.append("Joaquim") dá erro
#nomes[1] = "Marcelo" dá erro


#exercicio de boletim escolar com listas, tuplas, bimestre, notas