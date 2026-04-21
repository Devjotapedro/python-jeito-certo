from reportlab.lib import colors
from reportlab.graphics.shapes import (Drawing,
Rect)
OUT_DIR = "grafica"
WIDTH = 640
HEIGHT = 360

PG_COLORS = {
    "blue": colors.HexColor("#062846"),
    "green": colors.HexColor("#109395") 
}

def draw_background(drawing, margin=(16, 16), radius=32):
    #00 é a primeira coordenada
    #reetangulo externo
    outer_rect = Rect(0,0, WIDTH, HEIGHT, fillColor = PG_COLORS["green"])
    drawing.add(outer_rect)
    
    xmargin = margin[0]
    ymargin = margin[1]
    #retangulo interno
    inner_rect = Rect(xmargin,ymargin, WIDTH - 2 * xmargin, HEIGHT - 2 * ymargin, radius, radius, fillColor = PG_COLORS["blue"], strokeColor = PG_COLORS["blue"])
    drawing.add(inner_rect)

if __name__ == '__main__':

    drawing = Drawing(WIDTH, HEIGHT)
    #Desenha o fundo
    draw_background(drawing)
    # save
    drawing.save(formats=['pdf'], outDir=OUT_DIR, fnRoot="carteirinha")