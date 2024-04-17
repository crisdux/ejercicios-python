## imprimir los 100 primero numeros de la secuencia de fibonacii

def fibo(n):
    list_fibo = [0,1]
    for i in range(2, n):
        next_fibo = list_fibo[-2] + list_fibo[-1]
        list_fibo.append(next_fibo)
    return list_fibo
    
print(fibo(100))
        
    