#  Encuentre el máximo común divisor entre dos números enteros.                                                                      │
# │                                                                                                                                   │
# │ NOTAS:                                                                                                                            │
# │                                                                                                                                   │
# │  • No es necesario utilizar ningún algoritmo existente.                                                                           │
# │  • Basta con probar divisores.

def gcd(a, b):
    while a != 0 and b != 0:
        cociente = a //b
        resto = a % b
        
        a = b
        b = resto
        
        if a == 0:
            return b 
        if b == 0:
            return a
    
print(gcd(270, 192))   
print(gcd(1, 1))   
print(gcd(3, 7))   
print(gcd(46, 64))   
print(gcd(12, 44))   
print(gcd(28, 91))   