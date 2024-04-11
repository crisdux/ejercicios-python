# Necesitamos una función simple que determine si se necesita un plural o no. Debería tomar un número y devolver verdadero si se debe usar un plural con ese número o falso en caso contrario. Esto sería útil al imprimir una cadena como 5 minutes, 14 appleso 1 sun.

# Sólo debes preocuparte por las reglas gramaticales inglesas para este kata, donde todo lo que no es singular (uno de algo), es plural (no uno de algo).

# Todos los valores serán números enteros positivos o flotantes, o cero.

def plural(n):
    if n == 1 or n == 1.0:
        return False
    else:
        return True
        
print(plural(1))
print(plural(100))
        