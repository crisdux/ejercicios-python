# Escribe una función que verifique si dos caracteres dados son el mismo caso.

# Si alguno de los caracteres no es una letra, regresa-1
# Si ambos caracteres son el mismo caso, regresa1
# Si ambos caracteres son letras, pero no son el mismo caso, devuelve0

# 'a'y 'g'regresa1

# 'A'y 'C'regresa1

# 'b'y 'G'regresa0

# 'B'y 'g'regresa0

# '0'y '?'regresa-1

def check_letras(caracter1, caracter2):
    if (caracter1.islower() and caracter2.islower()) or (caracter1.isupper() and caracter2.isupper()):
        return 1 
    elif (caracter1.islower() and caracter2.isupper()) or (caracter1.isupper() and caracter2.islower()):
        return 0
    elif ( not caracter1.isalpha() or not caracter2.isalpha()):
        return -1
        
print(check_letras("a","g"))
print(check_letras("A","C"))
print(check_letras("b","G"))
print(check_letras("B","g"))
print(check_letras("0","?"))

        