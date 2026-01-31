nomes_arquivos = [
    "bola.png", "texto.txt", "page.pdf", "medalha.png"
]

#verificar se termona com png
#print("ninja.png".endswith(".png"))

# imagens = []
# for nome in nomes_arquivos:
#     if nome.endswith(".png"):
#         imagens.append(nome)

#list comprehension
imagens = [nome for nome in nomes_arquivos
           if nome.endswith(".png")]

print(imagens)
