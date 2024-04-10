# Todo el mundo conoce la clásica regla de las citas "la mitad de tu edad más siete" que mucha gente sigue (incluyéndome a mí). Es el rango de edad "recomendado" para salir con alguien.

# min = (edad / 2) + 7
# max = (edad - 7) * 2

# Dado un número entero (1 <= n <= 100) que representa la edad de una persona, devuelve su rango de edad mínimo y máximo.

# Esta ecuación no funciona cuando la edad <= 14, así que use esta ecuación en su lugar:

# min = age - 0.10 * age
# max = age + 0.10 * age

# Debes reducir todas tus respuestas para que se proporcione un número entero en lugar de un flotante (que no representa la edad).Return your answer in the form [min]-[max]

# age = 27   =>   20-40
# age = 5    =>   4-5
# age = 17   =>   15-20

import math 

def calculo_edades_min_max(edad):
    if edad < 0 or edad >100:
        print("Edad no permitida")
        return

    if edad <= 14:
        min = math.floor(edad - 0.10 * edad)
        max = math.floor(edad + 0.10 * edad)
        return f"{min}-{max}"
        
    min = math.floor((edad / 2) + 7)
    max = math.floor((edad - 7) * 2)
    return f"{min}-{max}" 
        
print(calculo_edades_min_max(5))
print(calculo_edades_min_max(27))
print(calculo_edades_min_max(17))
print(calculo_edades_min_max(-1))