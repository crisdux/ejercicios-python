# │ Dados dos vectores (listas) de la misma dimensión, utilice la función zip() para calcular su producto escalar.                    │
# │                                                                                                                                   │
# │ Ejemplo:                                                                                                                          │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │  v1 = [4, 3, 8, 1]                                                                                                                │
# │  v2 = [9, 2, 7, 3]                                                                                                                │
# │                                                                                                                                   │
# │  v1 · v2 = [4⋅9 + 3·2 + 8·7 + 1·3] = 101                                                                                          │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │ Nota:                                                                                                                             │
# │                                                                                                                                   │
# │  • Si los vectores tienen distinta dimensión habrá que devolver None.

def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        return None
    res = []
    for v1, v2 in zip(vector1, vector2):
        item = v1*v2
        res.append(item)
    return sum(res)
        
print(dot_product([4, 3, 8, 1], [9, 2, 7, 3]))
print(dot_product([9, 1, 2], [8, 7, 5]))
print(dot_product([4, 2], [8, 7, 3]))