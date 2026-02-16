import os

#1 pegar o nome dos arquivos
#2 pegar a extensão do arquivo para determinar o tipo
#3 criar pastas: imagens, audios, documentos, videos, outros
#4 mover arquivos para as pastas correspondentes


#find -> procura da esquerda para direito
#rfind -> procura da direita para esquerda

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf']

def pegar_extensao(nome):
    #achr o indice do ponto no fim
    index = nome.rfind('.')
    return nome[index:]

def organizar(diretorio):
    
    #criar pastas
    
    AUDIO_DIR = os.path.join(diretorio, "audios")
    IMAGENS_DIR = os.path.join(diretorio, "imagens")
    DOCS_DIR = os.path.join(diretorio, "documentos")
    VIDEOS_DIR = os.path.join(diretorio, "videos")
    OUTROS_DIR = os.path.join(diretorio, "outros")
    
    #criar as pastas
    
    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)
    
    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            #extensão do arquivo com letras minusculas
            extensao = str.lower(pegar_extensao(arquivo))
            print(arquivo, extensao)
            if extensao in audios_ext:
                nova_pasta = AUDIO_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCS_DIR
            else:
                nova_pasta = OUTROS_DIR
                
            #pegar o arquivo e mover para a pasta nova
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)
            print("Moveu:", velho, "->", novo)
        
#não deixar rodar se importado
if __name__ == '__main__':
    organizar('/home/jp/Downloads')