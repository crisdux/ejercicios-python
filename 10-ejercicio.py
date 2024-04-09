# │ La entrada será una cadena de texto con dos números separados por una coma. El primer número es el coeficiente y el segundo       │
# │ número es el exponente. Por ejemplo:                                                                                              │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │  3,2 --> 3x^2                                                                                                                     │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │ Para obtener la integral tenemos que añadir 1 al exponente y dividir el coeficiente por dicho número. En el ejemplo anterior:     │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │  3x^2 --> 1x^3                                                                                                                    │
# │                                                                                                                                   │
# │                                                                                                                                   │
# │ NOTA: No se puede utilizar la función split()

def find_integral(symbol):
    base = int(symbol[:symbol.find(",")])
    exponente = int(symbol[symbol.find(",")+1:])
    return f"{int(base/(exponente+1))}x^{exponente + 1}"
    
print(find_integral("3,2"))
print(find_integral("12,5"))
print(find_integral("20,1"))
print(find_integral("40,3"))
print(find_integral("90,2"))