# Dada una lista - que puede contener sublistas (con sólo en 1 nivel de anidamiento) - genere otra lista "aplanada".

def flatten_list(elements):
    flatten_elements = []
    for i in elements:
        if type(i) != list:
            flatten_elements.append(i)
        else:
            for j in i:
                flatten_elements.append(j)
    return flatten_elements
    
print(flatten_list( [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]] ))
print(flatten_list( ['a', ['b', 'c'], 'd'] ))
print(flatten_list([[1], [2], [3], [4]] ))