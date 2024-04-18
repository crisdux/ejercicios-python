# │ Escriba un programa en Python que acepte una cadena de texto e indique si todos sus caracteres son alfabéticos.                   │
# │                                                                                                                                   │
# │ NOTAS:                                                                                                                            │
# │                                                                                                                                   │
# │  • No usar la función isalpha()                                                                                                   │
# │  • Usar una constante: ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def isalphabetic(text):
    text = text.lower()
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    for i in text:
        if not (i in ALPHABET):
            return False
    return True
    
print(isalphabetic("hello-world"))
print(isalphabetic("Computer"))
print(isalphabetic("first_in_first_out"))
print(isalphabetic("Development"))
print(isalphabetic("Programming is fun!"))