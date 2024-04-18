# ╭──────────────────────────────────────────────── COMPROBANDO IGUALDAD DE POTENCIAS ────────────────────────────────────────────────╮
# │ Dado un valor entero positivo n compruebe que se cumple la siguiente igualdad:                                                    │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │           2                                                                                                                       │
# │  ⎛  n    ⎞      n                                                                                                                 │
# │  ⎜ ___   ⎟     ___                                                                                                                │
# │  ⎜ ╲     ⎟     ╲     3                                                                                                            │
# │  ⎜ ╱    k⎟  =  ╱    k                                                                                                             │
# │  ⎜ ‾‾‾   ⎟     ‾‾‾                                                                                                                │
# │  ⎝k = 1  ⎠    k = 1                                                                                                               │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │ → El objetivo es calcular ambos lados de la igualdad. Por ejemplo, para n=3 se cumple:                                            │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │             2    3    3    3                                                                                                      │
# │  (1 + 2 + 3)  = 1  + 2  + 3                                                                                                       │
# │                                                                                                                                   │
# ╰──────────────────────────────────



def case_1(n):
    x = 0
    for i in range(n+1):
        x +=i
    return x**2


def case_2(n):
    x = 0
    for i in range(n+1):
        x +=i**3 
    return x

def kpower(n):
    return [case_1(n), case_2(n)]
    
print(kpower(1))
print(kpower(2))
print(kpower(3))
print(kpower(4))
print(kpower(5))