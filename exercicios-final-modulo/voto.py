#Faça um programa que analisa um valor de idade de um indivíduo e responde se ele “é obrigado a votar”, “tem voto facultativo” ou “é proibido de votar”, usando os critérios adotados no Brasil. Você pode ignorar critérios não baseados na idade.

idade = int(input("Qual a sua idade?"))

if idade >= 18 and idade < 60:
    print("Voto obrigatório")
elif idade > 60 or idade >= 16:
    print("Voto facultativo")
else:
    print("Voto proibido")