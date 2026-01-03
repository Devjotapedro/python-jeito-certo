texto = "  9.0"
aux = texto.strip() #remove espaço em branco
partes = aux.split('.') #dibide em um caracter
print(partes)
eh_numero = True
if len(partes) <= 2:
    for parte in partes:
        print(parte)
        #verifica se cada parte é um digito
        if not parte.isdigit():
            eh_numero = False
else:
    eh_numero = False
    
if eh_numero:
    print("É número")
else:
    print("Não é número")