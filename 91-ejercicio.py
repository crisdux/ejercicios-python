# │ Utilizando listas por comprensión, cree una lista que contenga el resultado de aplicar la función f(x) = 3x + 2 para el rango de  │
# │ x dado en los valores de entrada.                                                                                                 │
# │                                                                                                                                   │
# │ Ejemplo: Si xmin=0 y xmax=5, la lista de valores resultante debería ser: [2, 5, 8, 11, 14]

def fcomp(xmin, xmax):
    return [ 3*i + 2 for i in range(xmin, xmax+1)]
    
print(fcomp(131,134))
print(fcomp(0, 10))