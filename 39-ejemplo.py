# Dada una matriz sin clasificar[ n1, n2, n3 ] de 3 números enteros positivos , determina si es posible formar una terna pitagórica usando esos 3 números enteros.

# Una terna pitagórica consiste en ordenar 3 números enteros, de manera que:

# a2 + b2 = c2

# Ejemplos
# [5, 3, 4] : es posible formar una terna pitagórica usando estos 3 números enteros: 3 2 + 4 2 = 5 2

# [3, 4, 5] : es posible formar una terna pitagórica usando estos 3 números enteros: 3 2 + 4 2 = 5 2

# [13, 12, 5] : es posible formar una terna pitagórica utilizando estos 3 números enteros: 5 2 + 12 2 = 13 2

# [100, 3, 999] : NO es posible formar una terna pitagórica usando estos 3 números enteros; no importa cómo los organices, nunca encontrarás una manera de satisfacer la ecuación a 2 + b 2 = c 2



def terna_pitagorica(lista):
    lista.sort()
    mayor = lista.pop()
    menor1 = lista[0]
    menor2 = lista[1]
    
    if mayor ** 2 == menor1 ** 2 + menor2 ** 2:
        return True
    else:
        return False
    
    
    
print(terna_pitagorica([5,3,4]))
print(terna_pitagorica([3,4,5]))
print(terna_pitagorica([13,12,5]))
print(terna_pitagorica([100,3,99]))