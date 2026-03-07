#atividade 2: sequencia de rolagem de dados (6 faces). rolar 10 dados (tirar a média e o desvio padrão e salvar em um arquivos), depois 100 dados no arquivos, depois 1000 dados, até 10000
import random
from math import pow, sqrt
#rolar dado

def rolar_dado(numero_dados):
    faces = []
    for _ in range(numero_dados):
        faces.append(random.randint(1,6))
    #print(f'faces: {faces}')
    return faces


#calcular media

def calc_media(faces):
    media = (sum(faces))/len(faces)
    #print(f'Média: {media:.2f}')
    return media

#calcular desvio padrão
def calc_desvio_padrao(faces, media):
    acc  = 0
    for face in faces:
        quadrado_diferenca = pow((face - media), 2)
        acc += quadrado_diferenca
    dp = sqrt((acc/len(faces)))
    #print(f'Desvio padrão: {dp:.2f}')
    return dp

#salvar em um arquivo

with open("dados.txt", "a") as arq:
    
    lances = [10, 100, 1000, 10000, 100000, 1000000]

    for lance in lances:
        face = rolar_dado(lance)
        media = calc_media(face)
        dp = calc_desvio_padrao(face, media)
    
        conteudo = f'Dados jogados: {len(face)} | Meida: {media:.2f} | Desvio padrão: {dp:.2f} \n'
        arq.write(conteudo)
