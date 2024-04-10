# convertir dolares a yuanes
# 1 dolar == 6.75 yuanes


def convertir_dolares_yuanes(cantidad_sus):
    if type(cantidad_sus) != int:
        print("Por favor, ingrese una cantidad entera de dólares.")
        return
    return cantidad_sus * 6.75
    

print(convertir_dolares_yuanes(15))
print(convertir_dolares_yuanes(465))