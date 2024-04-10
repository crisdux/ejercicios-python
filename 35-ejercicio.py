# Dado un mes como un número entero del 1 al 12, regrese a qué trimestre del año pertenece como un número entero.

# Por ejemplo: el mes 2 (febrero), forma parte del primer trimestre; el mes 6 (junio), forma parte del segundo trimestre; y el mes 11 (noviembre), forma parte del cuarto trimestre.

# Restricción:

# 1 <= month <= 12

def trimestres_anio(num_mes):
    if not (1 <= num_mes <= 12):
        print("el mes debe estar entre 1 y 12")
        return
    elif (1 <= num_mes <= 3):
        return "1er trimestre"
    elif (4 <= num_mes <= 6):
        return "2do trimestre"
    elif (7 <= num_mes <= 9):
        return "3er trimestre"
    else :
        return "4to trimestre"
    
print(trimestres_anio(1))
print(trimestres_anio(5))
print(trimestres_anio(8))
print(trimestres_anio(12))
print(trimestres_anio(-1))
    