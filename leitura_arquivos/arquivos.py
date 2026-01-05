#arquivo = open("mensagem.txt", "r") #passa o endereço do arquivo
#r abre o arquivo para leitura (read)
#msg = arquivo.read()
#fechar o arquivo
#arquivo.close()
#print(msg)

#outra forma de fazer (sem precisar fechar, pois so funciona escopo do open)
caminho = "/home/jp/dev/estudo/python-do-jeito-certo/python-jeito-certo/mensagem.txt"
#with open(caminho, "r") as arq:
    #m = arq.read()
#print(m)

#criar um arquivo (w -> write)
#arquivo = open("mensagem.txt", "w")

msg = "A nota de Matemática foi 9.0"
with open("mensagem.txt", "w") as arquivo:
    arquivo.write(msg)

#se não existe o arquivo é criado, se existe o arquivo é sobrescrito

#adicionando de forma "fake"
with open(caminho) as arq:
    conteudo = arq.read()
    
conteudo = conteudo + "\nA nota de História foi 9.7"

with open(caminho, 'w') as arq:
    arq.write(conteudo)