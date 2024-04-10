# Este kata consiste en multiplicar un número determinado por ocho si es par y por nueve en caso contrario.

def mult(a):
    if a%2 == 0:
        return a * 8
    else:
        return a *9
    
print(mult(4))
print(mult(7))