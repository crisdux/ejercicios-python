# Escribe un programa que encuentre la suma de cada número del 1 al num. El número siempre será un entero positivo mayor que 0. Su función solo necesita devolver el resultado, lo que se muestra entre paréntesis en el siguiente ejemplo es cómo llega a ese resultado y no es parte de él, consulte las pruebas de muestra.

# Por ejemplo (Entrada -> Salida) :

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

def summation(n):
    res=0
    for i in range(1, n+1):
        res += i
    return res
    
print(summation(2))
print(summation(8))

def summation_2(n):
    res = []
    for i in range(1, n+1):
        res.append(i)
    return sum(res)
    
print(summation_2(2))
print(summation_2(8))