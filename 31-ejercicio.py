# Los americanos son gente rara: en sus edificios, el primer piso es en realidad la planta baja y no existe el piso 13 (por superstición).

# Escribe una función que dado un piso en el sistema americano devuelva el piso en el sistema europeo.

# Con el reemplazo del primer piso por la planta baja y la eliminación del piso 13, los números se mueven hacia abajo para ocupar su lugar. En el caso de más de 13, bajan dos porque hay dos números omitidos debajo de ellos.

# Los sótanos (negativos) siguen siendo los mismos que el nivel universal.

def pisos_americanos_a_pisos_europeos(numero_pisos_americanos):
    if numero_pisos_americanos == 0:
        return 0
    elif numero_pisos_americanos < 0:
        return numero_pisos_americanos
    elif 1 <= numero_pisos_americanos <= 13:
        return numero_pisos_americanos - 1
    else:
        return numero_pisos_americanos - 2
        
print(pisos_americanos_a_pisos_europeos(1))
print(pisos_americanos_a_pisos_europeos(0))
print(pisos_americanos_a_pisos_europeos(5))
print(pisos_americanos_a_pisos_europeos(15))
print(pisos_americanos_a_pisos_europeos(-3))
    