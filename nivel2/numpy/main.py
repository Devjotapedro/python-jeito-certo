import numpy as np

v1 = np.array([3, 5, 7])
v2 = np.array([-1, 3, -4])

#com listas faz concatenação, com o método array, faz soma vetorial
#print(v1 + v2)

#exercicio

if __name__ == '__main__':
    a = np.array((2,5))
    b = np.array((1.5, 7.0))
    num = 4
    print('Soma dos vetores a e b: ', a+b)
    print('Diferença dos vetores a e b: ', a-b)
    print(f'Multiplicação de {a} por {num}: ', num*a)
    print('Produto escalar entre a e b: ', np.dot(a,b))
    
    #media
    print('média dos valores em a', a.mean())
    
    #construindo matrizes
    
    mat1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
    #matriz identidade
    mat2 = np.eye(3, 3)
    print(mat1)
    print(mat2)
    #produto de matrizes
    print(mat1 @ mat2)
    
    #maior valor
    print('Maior valor em mat1:', mat1.max())
    
#exercicios:

#1- gerar uma quantidade de pontos em um intervalo
#ex: gerar 10 pontos entre -1 e 1

#2- aplicar alguma função em cima desses pontos, como cos (sem usar for)

#salvar tudo em um arquivo

#exercicio 2:
#usar o pillow para gerar um quadrilátero. gerar uma matriz de rotação de um angulo com numpy
#ex: 45 graus. Rotacionar o quadrilátero