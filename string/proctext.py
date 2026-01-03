texto = "matematica"
#acessando um caractere específico
print(texto[0]) #m
#ultima letra
print(texto[-1])
print(texto[len(texto) - 1])

#iterando sobre uma string

for c in texto:
    print(c)
    
print("---------------------------------")

#comparando strings

print("matematica" == texto) #True

#convertendo para maiuscula
print("matematica".upper())

#convertendo para minuscula
print("matematica".lower())

#verificar se está contido

frase = "A nota de matematica de Pedro foi 7.9"

if texto.lower().strip() in frase.lower():
    print("Achou", texto)
else:
    print("Não ta aqui")
    

#remover os espaços: .strip() no inicio e final da string

#particionar uma string

partes = frase.split('m') #se adicionar um caractere, dá para espacionar nesse caracter
print(partes)

#exercicio: dizer se a string é um número ou não (inteiro ou float)

#isdigit verifica se na string há numeros. Se for float ele dá true por conta do ponto
text = "78"
print(text.isdigit())