# La conjetura de Collatz (también conocida como conjetura 3n+1) es una conjetura que aplicando el siguiente algoritmo a cualquier número siempre llegaremos a uno:

# [This is writen in pseudocode]
# if(number is even) number = number / 2
# if(number is odd) number = 3*number + 1
# #Tarea

# Su tarea es crear una función hotpoque tome un valor positivo ncomo entrada y devuelva la cantidad de veces que necesita realizar este algoritmo para obtenerlo n = 1.

# #Ejemplos

# hotpo(1) returns 0
# (1 is already 1)

# hotpo(5) returns 5
# 5 -> 16 -> 8 -> 4 -> 2 -> 1

# hotpo(6) returns 8
# 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# hotpo(23) returns 15
# 23 -> 70 -> 35 -> 106 -> 53 -> 160 -> 80 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

def hotpo(n):
    c = 0
    while n != 1:
        if n % 2 !=0:
            n = (3*n)+1 
            c = c + 1
        elif n % 2 == 0:
            n = n//2
            c = c + 1 
    return c 
    
    
print(hotpo(1))
print(hotpo(5))
print(hotpo(6))
print(hotpo(23))