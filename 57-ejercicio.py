# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

def hacia_atras(n):
    for i in range(n, 0, -1):
        print(i, end= ",")
        
print(hacia_atras(10))
    
        