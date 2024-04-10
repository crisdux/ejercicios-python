#convierte un numero a negativo, si el numero dado es negativo ya solo regresalo 
def convierte_negativo(numero):
    if numero < 0:
        return numero
    elif (numero > 0):
        return numero * -1
    
print(convierte_negativo(1))
print(convierte_negativo(-5))
print(convierte_negativo(0))