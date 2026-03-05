import random

aleatorio = random.randint(1, 100)

chute = int(input("Advinhe o valor (entre 0 e 1000): "))

while chute != aleatorio:
    if chute > aleatorio:
        print("Seu chute foi maior que o número escolhido")
    elif chute < aleatorio:
        print("Seu chute foi menor que o número escolhido")
    chute = int(input("Digite o seu chute: "))
print(f"Parabéns! Você acertou, o número era {aleatorio}")