# Te dan el lengthy widthde un polígono de 4 lados. El polígono puede ser un rectángulo o un cuadrado.
# Si es un cuadrado, devuelve su área. Si es un rectángulo, devuelve su perímetro.

# Ejemplo (Entrada1, Entrada2 --> Salida):

# 6, 10 --> 32
# 3, 3 --> 9

# Nota: para los propósitos de este kata asumirás que es un cuadrado si lengthy widthson iguales; de lo contrario, es un rectángulo.

def poligonos(length, width):
    if length == width:
        return length ** 2
    else:
        return length * 2 + width * 2
    
print(poligonos(6,10))
print(poligonos(3,3))