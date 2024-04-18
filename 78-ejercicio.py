
# Escriba una función que tome un número entero como entrada y devuelva el número de bits que son iguales a uno en la representación binaria de ese número. Puede garantizar que la entrada no sea negativa.

# Ejemplo : la representación binaria de 1234es 10011010010, por lo que la función debería regresar 5en este caso

def count_bits(n):
    x = bin(n)
    return (str(x)[2:]).count("1")
    
print(count_bits(1234))