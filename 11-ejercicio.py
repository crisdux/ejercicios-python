# A Jack le gusta hacer una multiplicación muy particular: Dado un número n multiplica n por 5 elevado al número de dígitos de n.                                                                                                                                 │
# Por ejemplo:
# n = 10 -> 10 * 5²

def multiply_jack(n):
    if n > 0:
        return (n * (5) ** len(str(n)) )
    else:
        return (n * (5) ** len(str(n * -1)) )

print(multiply_jack(3))
print(multiply_jack(10))
print(multiply_jack(200))
print(multiply_jack(0))
print(multiply_jack(-3)) 
