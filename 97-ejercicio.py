# Dada una lista de entrada, devuelva True si todos sus elementos son iguales o False en otro caso. 

def all_same(items):
    for i, value in enumerate(items):
        if value == items[i-1]:
            return True
        return False
        
        
print(all_same([1,1,1,1,1,1]))
print(all_same([1,1,1,1,1,2]))
print(all_same( ['a', 'b', 'c']))