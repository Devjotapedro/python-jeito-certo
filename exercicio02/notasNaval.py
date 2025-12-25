#refazer lógica de notas do colégio naval

nota = 5
media_baixa = 5
media_alta = 7

if nota >= media_alta:
    print("Passei direto")
    
elif nota >= media_baixa:
    print("Prova final")
    
    nota_pf = 4
    if nota_pf >= media_baixa:
        print("Aprovado na prova final")
    else:
        print("Precisa fazer a recuperação")
        
        nota_rf = 5
    if nota_rf >= media_baixa:
        print("Aprovado na recuperação final")
    else:
        print("Reprovado")
        
else:
    print("Recuperação final")
    nota_rf = 5
    
    if nota_rf >= media_baixa:
        print("Aprovado na recuperação final")
    else:
        print("Reprovado")
    