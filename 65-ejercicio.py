# Escriba un programa que pida nombre y apellidos de una persona (usando un solo
# input) y repita la pregunta mientras el nombre no esté en formato título (solución).

# ¿Su nombre? ana torres blanco
# Error. Debe escribirlo correctamente
# ¿Su nombre? Ana torres blanco
# Error. Debe escribirlo correctamente
# ¿Su nombre? Ana Torres blanco
# Error. Debe escribirlo correctamente
# ¿Su nombre? Ana Torres Blanco

def nombre_correcto():
    nombre_completo = input("Escriba su nombre ")
    while not nombre_completo.istitle():
        print("incorrecto")
        nombre_completo = input("Escriba su nombre ")
        
    print("Correcto")
    
print(nombre_correcto())
