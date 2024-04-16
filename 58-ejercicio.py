# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# *
# **
# ***
# ****
# *****

def estrella(x):
    for i in range(1, x+1):
        print(f"*"*i)
    return ""
print(estrella(5))