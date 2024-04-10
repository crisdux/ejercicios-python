#  Acepte la opción de dos jugadoras en Piedra-Papel-Tijera y decida el resultado final.                                             │
# │                                                                                                                                   │
# │ NOTAS:                                                                                                                            │
# │                                                                                                                                   │
# │  • La entrada siempre vendrá en forma de string con valores 'piedra', 'papel' o 'tijera', pero puede estar en mayúsculas,         │
# │    minúsculas o mezcla de ellas.                                                                                                  │
# │  • La salida deberá de ser un valor numérico entero:                                                                              │
# │     • 1 si gana la primera jugadora.                                                                                              │
# │     • 2 si gana la segunda jugadora.                                                                                              │
# │     • 0 si hay empate.

def rps(choise1, choise2):
    choise1 = choise1.lower()
    choise2 = choise2.lower()
    
    if choise1 == choise2:
        return 0
    elif (choise1 == "piedra" and choise2 == "tijera") or (choise1 == "papel" and choise2 =="piedra") or (choise1 == "tijera" and choise2 == "papel"):
        return 1 
    else:
        return 2

print(rps("piedra", "PAPEL"))
print(rps("tijera", "papel"))
print(rps("papel", "papel"))