import getpass
#modulo para esconder a senha

#constantes
EMPATE = 0
VIT_JOGADOR1 = 1
VIT_JOGADOR2 = 2


def pre_processar_resposta(escolha):
    return escolha.lower().strip()

def solicitar_escolhas():
    escolhas = []
    for i in range(1, 3):
        escolha = getpass.getpass(f"Jogador {i} - Escolha 'pedra', 'papel' ou 'tesoura': ")
        escolhas.append(pre_processar_resposta(escolha))
    return escolhas
    
    
def jokenpo(jogador1, jogador2):

    jogador1 = pre_processar_resposta(jogador1)
    jogador2 = pre_processar_resposta(jogador2)

    if jogador1 == jogador2:
        return EMPATE
    elif ((jogador1 == 'pedra' and jogador2 == 'tesoura') or
        (jogador1 == 'tesoura' and jogador2 == 'papel') or
        (jogador1 == 'papel' and jogador2 == 'pedra')
        ):
        return VIT_JOGADOR1
    else:
        return VIT_JOGADOR2
        
escolhas = solicitar_escolhas()
resultado = jokenpo(escolhas[0], escolhas[1])

#enumerate: captura o indice e o valor do elemento

for i, escolha in enumerate(escolhas):
    print(f"jogador {i + 1}: {escolha}")
print("\n Resultado: ")

if resultado == EMPATE:
    print("Empate!")
elif resultado == VIT_JOGADOR1:
    print("Jogador 1 venceu!")
else:
    print("JOgador 2 venceu!")