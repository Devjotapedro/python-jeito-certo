from PIL import Image, ImageDraw
import numpy as np

LARGURA = 400
ALTURA = 400

PONTOS = [
    (100, 100),
    (200, 100),
    (220, 200),
    (120, 220)
]

WHITE = (255, 255, 255)

# função para criar e desenhar os quadriláteros
def criarQuadrilatero(largura, altura, pontos_originais, pontos_rotacionados):
    # criar imagem
    imagem = Image.new("RGB", (largura, altura), WHITE)
    
    # criar desenhador
    draw = ImageDraw.Draw(imagem)
    
    # desenhar quadrilátero original (preto)
    draw.polygon(pontos_originais, outline="black")
    
    # desenhar quadrilátero rotacionado (vermelho)
    draw.polygon(pontos_rotacionados, outline="red")
    
    # mostrar imagem
    imagem.show()


# função de rotação
def rotacionar_pontos(pontos, angulo):
    rad = np.radians(angulo)
    
    # matriz de rotação
    R = np.array([
        [np.cos(rad), -np.sin(rad)],
        [np.sin(rad),  np.cos(rad)]
    ])
    
    pontos_np = np.array(pontos)
    
    # calcular centro
    centro = pontos_np.mean(axis=0)
    
    novos_pontos = []
    
    for p in pontos_np:
        # centraliza
        p_centralizado = p - centro
        
        # rotaciona (@ multiplicação de matrizes)
        p_rotacionado = R @ p_centralizado
        
        # volta para posição original
        p_final = p_rotacionado + centro
        
        # converter para inteiro
        novos_pontos.append(tuple(map(int, p_final)))
        
    return novos_pontos


# ângulo de rotação
angulo = 45

# calcular pontos rotacionados
pontos_rotacionados = rotacionar_pontos(PONTOS, angulo)

# desenhar tudo
criarQuadrilatero(LARGURA, ALTURA, PONTOS, pontos_rotacionados)