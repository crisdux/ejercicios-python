# Tu trabajo
# Encuentra la suma de todos los múltiplos de nabajom

# Tenga en cuenta
# ny mson números naturales (enteros positivos)
# mestá excluido de los múltiplos

def sum_mul(n,m):
    if n <= 0 or m <=0:
        return "INVALID"
        
    res = 0
    for i in range(n, m, n):
        res += i
    return res
    
    
print(sum_mul(0,0))
print(sum_mul(2,9))

print(sum_mul(4,-7))
print(sum_mul(4,123))
print(sum_mul(123,4567))
