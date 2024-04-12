# El número n es Maligno si tiene un número par de unos en su representación binaria.
# Los primeros números malvados: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20

# El número n es Odioso si tiene un número impar de unos en su representación binaria.
# Los primeros números Odious: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19

# Tienes que escribir una función que determine si un número es Evil of Odious, la función debería devolver "¡Es malvado!" en caso de número malvado y "¡Es odioso!" en caso de número odioso.

# buena suerte :)

def evil(n):
    decimal_a_binario = bin(n)[2:]
    
    cantidad_unos = int(decimal_a_binario.count("1"))
    if cantidad_unos % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
    
print(evil(10))