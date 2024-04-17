# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def contar_letras(frase, letra):
    frase = frase.lower()
    return frase.count(letra)
    
print(contar_letras("hola mundo", "o"))