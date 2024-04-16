# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

def numeros_impares(n):
    impares = ""
    for i in range(1, n+1):
        if i % 2 != 0:
            impares += str(f"{i},")
    return impares[:-1]
            
print(numeros_impares(11))
print(numeros_impares(20))
print(numeros_impares(1))
        