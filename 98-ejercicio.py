# │ Escriba un programa en Python que acepte una lista de listas representando una matriz numérica de valores enteros y  │
# │ compute la suma de los elementos de la diagonal principal.                                                           │
# │                                                                                                                      │
# │ Notas:                                                                                                               │
# │                                                                                                                      │
# │  • Si no se trata de una Matriz cuadrada devuelva None.                                                              │
# │  • Puede afrontar el ejercicio en versión clásica o con listas por comprensión. ¡O incluso ambas!

def sum_diagonal(matrix):
    if len(matrix) != len(matrix[0]):
        return None
    res = []
    for i, value in enumerate(matrix):
        res.append(matrix[i][i])
    return sum(res)
    
print(sum_diagonal([[4, 6, 1], [2, 9, 3], [1, 7, 7]]))
print(sum_diagonal([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]]))