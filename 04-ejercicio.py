#  Dado un número entero n compute el valor de n + nn + nnn                                                                          │
# │                                                                                                                                   │
# │ Notas:                                                                                                                            │
# │                                                                                                                                   │
# │  • Por ejemplo, si n=2 hay que calcular: 2 + 22 + 222 = 246                                                                       │
# │  • Contemplar únicamente n en el intervalo [0,9]

def n_repeat(n):
    n = int(input("Escriba un numero entre 0 y 9: "))
    while n < 0 or n > 9:
        n = int(input("Escriba un numero entre 0 y 9: "))
    nn = int(f"{n}{n}")
    nnn = int(f"{n}{n}{n}")
    return int(n) + nn + nnn
    
print(n_repeat("2")) ## 246
print(n_repeat("3")) ## 369
print(n_repeat("4")) ## 492
print(n_repeat("5")) ## 615