#  Dada una lista de valores numéricos enteros, obtenga su máximo valor.                                                             │
# │                                                                                                                                   │
# │ Implementa la solución usando la función "built-in" min().                                                                        │
# │                                                                                                                                   │
# │ Prohibido utilizar:                                                                                                               │
# │                                                                                                                                   │
# │  • La función "built-in" max().                                                                                                   │
# │  • La función "built-in" sorted().

def min_list(my_list):
    while len(my_list) != 1:
        min_item = min(my_list) # 3
        my_list.remove(min_item)
    return my_list[0]
    
print(min_list( [-11, 10, -6, 15, -1]))
print(min_list([5, 9, -6, 9, -2, -9, -7, 2]))
print(min_list([-7, -5, -5, -8, -3]))
