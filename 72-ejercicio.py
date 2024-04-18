# │ Dado un número entero calcule el producto acumulado de cada valor al cuadrado hasta llegar a dicho número.                        │
# │                                                                                                                                   │
# │ Por ejemplo, si n=4 el resultado saldría del siguiente cálculo:                                                                   │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │   2    2    2    2                                                                                                                │
# │  1  ⋅ 2  ⋅ 3  ⋅ 4  = 576

def cumsq_prod(n):
    res = 1
    for i in range(1, n+1):
        res *= i**2 
    return res
        
print(cumsq_prod(4))
print(cumsq_prod(7))
print(cumsq_prod(10))