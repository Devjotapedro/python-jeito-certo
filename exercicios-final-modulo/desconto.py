#Implemente um programa que dá um desconto de 12% sobre o preço de um item à venda, exibindo o valor final e o desconto.

item = 150000
desconto = 12
novoValor = item - (item * desconto)/100
print(f"Seu produto de R$ {item} reais, terá um desconto de {desconto} por cento. Seu novo valor será de R$ {novoValor} reais")