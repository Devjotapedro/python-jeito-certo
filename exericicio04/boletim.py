boletim = [
    ["portugues", "matematica", "fisica"], 
    [80, 100, 100], 
    [70, 80, 60],
    [75, 90, 85],
    [90, 100, 100]
    ]

print(f"As suas notas em {boletim[0][0]} foram {boletim[1] [0]}, {boletim[2] [0]}, {boletim[3][0]}, {boletim[4] [0]}")
print(f"As suas notas em {boletim[0][1]} foram {boletim[1] [1]}, {boletim[2] [1]}, {boletim[3][1]}, {boletim[4] [1]}")
print(f"As suas notas em {boletim[0][2]} foram {boletim[1] [2]}, {boletim[2] [2]}, {boletim[3][2]}, {boletim[4] [2]}")


mediaPortugues = (boletim[1][0] + boletim[2][0] + boletim[3][0] + boletim[4][0])/4
print(f"A sua média em {boletim[0][0]} é {mediaPortugues}")

mediaMatematica = (boletim[1][1] + boletim[2][1] + boletim[3][1] + boletim[4][1])/4
print(f"A sua média em {boletim[0][1]} é {mediaMatematica}")

mediaFisica = (boletim[1][2] + boletim[2][2] + boletim[3][2] + boletim[4][2])/4
print(f"A sua média em {boletim[0][2]} é {mediaFisica}")