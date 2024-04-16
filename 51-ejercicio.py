# Basic regex tasks. Write a function that takes in a numeric code of any length. The function should check if the code begins with 1, 2, or 3 and return true if so. Return false otherwise.

# You can assume the input will always be a number.

import re

def verificar_inicio(numero):
    # Convertir el número a cadena
    numero_str = str(numero)
    
    # Definir el patrón de regex para verificar el inicio del número
    patron = r'^[1-3]\d*'
    
    # Utilizar la función fullmatch() para verificar si el número coincide completamente con el patrón
    if re.fullmatch(patron, numero_str):
        return True
    else:
        return False

# Ejemplos de uso
print(verificar_inicio(123))   # True
print(verificar_inicio(456))   # False
print(verificar_inicio(2567))  # True
print(verificar_inicio(11))    # False (No comienza con 1, 2 o 3)