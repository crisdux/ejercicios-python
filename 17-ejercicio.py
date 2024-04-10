# Dados 3 números calcule el mínimo.

def min3values(value1, value2, value3):
    list_nums = [value1, value2, value3]
    return min(list_nums)
    
print(min3values(7,4,9))
print(min3values(2,5,1))
print(min3values(9,3,7))
print(min3values(9,9,9))