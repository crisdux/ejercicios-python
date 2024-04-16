# escribir una función que dado un numero regrese todos los multiplos menores a ese numero

def f(n):
    aux = 5
    r = []
    while aux <= n:
        r.append(aux)
        aux +=5
    return r
print(f(36))