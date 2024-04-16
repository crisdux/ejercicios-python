# escribir una funcion que regrese si un numero es primo o no
def is_prime(num):
    if num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
    
print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(6))
print(is_prime(7))
print(is_prime(8))
print(is_prime(9))
print(is_prime(10))