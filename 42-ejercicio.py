# Crea una función llamada close_compare que acepte 3 parámetros: a, b y un margen opcional. La función debería devolver si a es menor que, cercano a, o mayor que b.

# Por favor, ten en cuenta lo siguiente:

# Cuando a está cercano a b, devuelve 0.
# Para este desafío, se considera que a está "cercano a" b si el margen es mayor o igual a la distancia absoluta entre a y b.
# De lo contrario...

# Cuando a es menor que b, devuelve -1.

# Cuando a es mayor que b, devuelve 1.

# Si no se proporciona margen, trátalo como si fuera cero.

# Supón: margen >= 0

# Consejo: Algunos lenguajes tienen una forma de hacer que los parámetros sean opcionales.



def close_compare(a, b, margin = 0):
    distancia = abs(a - b) 
    if margin >= distancia:
        return 0
    elif a < b:
        return -1
    else:
        return 1 
        
print(close_compare(3,5,3))
print(close_compare(3,5))
    