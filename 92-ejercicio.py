# │ Dada una lista de valores numéricos enteros, obtenga su máximo valor.                                                │
# │                                                                                                                      │
# │ Prohibido utilizar:                                                                                                  │
# │                                                                                                                      │
# │  • La función "built-in" min().                                                                                      │
# │  • La función "built-in" max().                                                                                      │
# │  • La función "built-in" sorted().

def max_value(list_numbers):
    max_value = list_numbers[0]
    
    for number in list_numbers:
        if number > max_value:
            max_value = number
    return max_value
print(max_value([-11, 10, -6, 15, -1]))