from modulo_vetores import capturar_vetores, soma_vetores, subtrai_vetores, multiplica_escalar, produto_escalar

while True:
    print('---------------------')
    print('Menu')
    print('---------------------')
    print('Digite 1 para somar vetores')
    print('Digite 2 para subtrair vetores')
    print('Digite 3 para multiplicar por uma constante')
    print('Digite 4 para multiplicar vetores')
    print('Digite 5 para sair')
    
    num = int(input('Digite um número :'))
    
    if num == 1:
        v1, v2 = capturar_vetores()
        soma_vetores(v1, v2)
    elif num == 2:
        v1, v2 = capturar_vetores()
        subtrai_vetores(v1, v2)
    elif num == 3:
        v1, v2 = capturar_vetores()
        multiplica_escalar(v1)
    elif num == 4:
        v1, v2 = capturar_vetores()
        produto_escalar(v1, v2)
    elif num == 5:
        print('---------------------')
        print("Saindo do programa")
        print('---------------------')
        
        break;
    else:
        print("Digite um valor válido")
        