#  Dada una cadena de texto, indique el número de vocales que tiene.                                                                 │
# │                                                                                                                                   │
# │ NOTA:                                                                                                                             │
# │                                                                                                                                   │
# │  • No se puede utilizar la función count()

def contador(text):
    text = text.lower()
    contador = 0
    vocales = "aeiouáéíóú"
    for letra in text:
        if letra in vocales:
            contador = contador + 1
    return contador
    
print(contador("El camión chocó contra el árbol"))
print(contador("WELCOME HOME"))
print(contador("Órbita Laica"))
print(contador("Programar va de pensar, no de escribir"))
print(contador("Simple es mejor que complejo"))