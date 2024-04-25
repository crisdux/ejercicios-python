#  Dada una lista, genere otra lista eliminando los elementos duplicados consecutivos.  

def remove_consecutive_dups(items):
    res = [] # 0
    for i, value in enumerate(items):
        if i == 0 or value != items[i-1]:
            res.append(items[i])
    return res
        
print(remove_consecutive_dups([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))
print(remove_consecutive_dups([1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]))