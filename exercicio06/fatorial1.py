#1- input que recebe numero positivo maior que 0
#2- laço de repetição decrescente até esse numero multiplicando pelo anterior
#3- exibir o calculo e o valor

numero = int(input("Digite um número: "))
original = numero
total = 1

while numero < 0:
    numero = int(input("Digite um número positivo: "))

while numero >= 1:
    total = numero * total
    print(f"{numero} x ")
    numero = numero - 1
    
    

print(f"O fatorial de {original} é {total}")