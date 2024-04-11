# Los niños beben ponche.
# Los adolescentes beben cocaína.
# Los adultos jóvenes beben cerveza.
# Los adultos beben whisky.
# Haz una función que reciba edad y devuelva lo que beben.

# Normas:

# Niños menores de 14 años.
# Adolescentes menores de 18 años.
# Jóvenes menores de 21 años.
# Los adultos tienen 21 o más.
# Ejemplos: (Entrada --> Salida)

# 13 --> "drink toddy"
# 17 --> "drink coke"
# 18 --> "drink beer"
# 20 --> "drink beer"
# 30 --> "drink whisky"


def bebidas(edad):
    if edad < 14:
        return "drink toddy"
    elif 14 <= edad <= 17:
        return "drink coke"
    elif 18 <= edad <=20:
        return "drink beer"
    else:
        return "drink whisky"
        
print(bebidas(13))
print(bebidas(17))
print(bebidas(18))
print(bebidas(20))
print(bebidas(30))
    