# Dada una lista de enteros y enteros como cadenas de texto, calcule la suma de todos los valores de la lista como si  │
# │ todos sus elementos fueran números.

def sum_mixed(items):
    nums_items= []
    
    for i in items:
        if type(i) == str:
            nums_items.append(int(i))
        else:
            nums_items.append(i)
    return sum(nums_items)
    
print(sum_mixed([1, '2', 3, '4', 5]))
print(sum_mixed(['0', '-1', '-2', '-3', '-4', '-5']))
print(sum_mixed([100, 90, 80, 70, '60', '50', '40', '30', '20', '10']))