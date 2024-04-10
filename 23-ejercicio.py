## te dan 2 angulos internos de un triangulo. Encuentra el 3ro

def calcular_angulo(alfa, beta):
    if type(alfa) != int or type(beta) != int:
        print("Error... deben ser enteros ")
        return
    return 180 -alfa-beta

print(calcular_angulo(60,50))
print(calcular_angulo("60",50))