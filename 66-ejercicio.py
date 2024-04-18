# Escriba un programa en Python que realice las siguientes 9 multiplicaciones. ¿Nota
# algo raro en el resultado? (solución)
# 1 · 1
# 11 · 11
# 111 · 111
# .
# .
# .
# 111111111 · 111111111

def mult():
    for i in range(1, 10):
        x = int("1" * i)
        print( f"{x} x {x} = {x*x}")
            
print(mult())