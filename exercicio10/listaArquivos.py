#ir adicionando em uma lista todas as strings (append)
#exibir no arquivo essas strings

lista = []
programa = input("digite 1 para iniciar o programa ou qualquer tecla para encerrar: ")
if programa == "1":
    while True:
        fruta = input("digite uma fruta: ")
        lista.append(fruta + "\n")
        programa = input("Deseja adicionar outra fruta?(sim/nao) ")
        if programa != "sim":
            print("----------Encerrando------------")
            break
    print(lista)
    

with open("listaFrutas.txt", "a") as list:
    list.writelines(lista)