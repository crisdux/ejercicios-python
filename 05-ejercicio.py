# Calcule la siguiente métrica para una cadena de texto dada: Número total de caracteres multiplicado por número total de vocales.

def counter_vocales(text):
    vocales = ["a", "e", "i", "o", "u"]
    c = 0
    for letra in text.lower():
        for vocal in vocales:
            if vocal == letra:
                c = c + 1
    return c
    
def str_metric(text):
    return len(text) * counter_vocales(text)
    
print(str_metric("ordenador")) ## 36
print(str_metric("pantalla")) ## 24 
print(str_metric("procesador")) ## 40