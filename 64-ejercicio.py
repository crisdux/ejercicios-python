#tablas de multiplicar

def tablas_multiplicar(n):
    print("tablas de multiplicar")
    for i in range(1, n+1):
        print("")
        for j in range(1, n+1):
            print(f"{i} x {j} = {i*j}")
            
            
print(tablas_multiplicar(10))