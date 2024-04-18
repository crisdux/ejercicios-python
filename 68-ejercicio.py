# Escriba un programa que muestre por pantalla todas las fichas del dominó. La ficha
# «en blanco» se puede representar con un 0 (solución).

def domino():
    for i in range(7):
        for j in range(7):
            if i <= j:
                print(f"{i}|{j}", end=" ")
        print()
    
print(domino())