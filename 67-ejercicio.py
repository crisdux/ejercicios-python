# Dado su tamaño, muestre por pantalla un mosaico donde la diagonal principal esté
# representada por X, la parte inferior por D y la parte superior por U

# • Entrada: 5

# • Salida:
# X U U U U
# D X U U U
# D D X U U
# D D D X U
# D D D D X




def cuadrante(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                print("X", end=" ")
            elif i<j:
                print("U", end= " ")
            else:
                print("D", end= " ")
        print("") 
                
print(cuadrante(10))
 