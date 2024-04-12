# Cuando se le proporcione un número entre 0 y 9, devuélvalo en palabras.

# Entrada :: 1

# Salida :: "Uno".

 
def convertir_a_palabras(numero):
    match(numero):
        case 0:
            return "Cero"
        case 1:
            return "Uno"
        case 2:
            return "Dos"
        case 3:
            return "Tres"
        case 4:
            return "Cuatro"
        case 5:
            return "Cinco"
        case 6:
            return "Seis"
        case 7:
            return "Siete"
        case 8:
            return "Ocho"
        case 9:
            return "Nueve"
        case _:
            "Número no válido"

    

# Ejemplo de uso
print(convertir_a_palabras(1)) 
print(convertir_a_palabras(3)) 
print(convertir_a_palabras(7)) 
print(convertir_a_palabras("7")) 
