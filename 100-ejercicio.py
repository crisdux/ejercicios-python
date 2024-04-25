#  Convierta un número decimal entero a su representación binaria (como string).                                        │
# │                                                                                                                      │
# │ No está permitido:                                                                                                   │
# │                                                                                                                      │
# │  • Utilizar la función bin()                                                                                         │
# │  • Utilizar f-strings con formato binario

def dec2bin(num):
    res = ""
    while num // 2 != 0 or num == 1:
        res += str(num % 2)
        num = num //2
    return res[::-1]

print(dec2bin(42))
print(dec2bin(23519))

