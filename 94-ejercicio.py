#  Dada una lista de números, obtenga otra lista donde se eliminen los duplicados. Mantenga el orden de los números en la lista de   │
# │ salida tal y como aparecen en la de entrada.

def remove_dups(nums_dups):
    nums_unique = [nums_dups[0]]
    for num in nums_dups[1:]:
        if num not in nums_unique:
            nums_unique.append(num)
        else:
            continue
    return nums_unique
    
print( remove_dups([2, 3, 2, 2, 1, 5, 4, 2, 4, 9]))
print( remove_dups([0, 9, 0, 9, 0, 9]))
print( remove_dups([1, 2, 3, 4, 5, 4, 3, 2, 1]))