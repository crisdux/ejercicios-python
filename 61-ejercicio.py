# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

def reverso_palabra(text):
    text_reverse = text[::-1]
    for item in text_reverse:
        print(item)
        
print(reverso_palabra("hola"))
    
    