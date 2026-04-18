import numpy as np

#constantes

INICIO = -1
FIM = 1
PONTOS = 10
ARQUIVO = 'arquivo_exe03.txt'

def gerarValores(inicio, fim, pontos):
    valores = np.linspace(inicio, fim, pontos)
    #print(valores)
    return valores

def calcCos(valores):
    res_cos = np.cos(valores)
    #print(cos)
    return res_cos
        
def salvarDados(valores, res_cos, ARQUIVO):
    res = np.column_stack((valores, res_cos))
    np.savetxt(ARQUIVO, res, delimiter="; ", header="X;cos(X)", comments="")
    #print(res)

def main():
    val = gerarValores(INICIO,FIM, PONTOS)
    valor_cos = calcCos(val)
    salvarDados(val, valor_cos, ARQUIVO)
    
if __name__ == '__main__':
    main()