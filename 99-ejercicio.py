# │ Dado un número entero no negativo obtenga una lista con todas las potencias de 2 con el exponente variando desde 0   │
# │ hasta dicho valor (inclusive).                                                                                       │
# │                                                                                                                      │
# │ ¿Podrías resolverlo también con listas por comprensión?

def powers2(num_powers):
    if num_powers < 0:
        return None
    res = []
    exponentes = []
    for exp in range(0, num_powers+1):
        exponentes.append(exp)
    bases = [ 2 for _ in range(len(exponentes))]
    
    for b, e in zip(bases, exponentes):
        res.append(b**e)
    return res
    
    
print(powers2(0))
print(powers2(1))
print(powers2(2))
print(powers2(-1))
    