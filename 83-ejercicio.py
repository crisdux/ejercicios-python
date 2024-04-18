# Su jefe decidió ahorrar dinero comprando un software de reconocimiento óptico de caracteres de precio reducido para escanear el texto de novelas antiguas en su base de datos. Al principio parece capturar bien las palabras, pero rápidamente notas que arroja muchos números en lugares aleatorios del texto.

# Ejemplos (entrada -> salida)
# '! !'                 -> '! !'
# '123456789'           -> ''
# 'This looks5 grea8t!' -> 'This looks great!'
# Tus acosados ​​compañeros de trabajo te buscan para encontrar una solución para tomar este texto confuso y eliminar todos los números. Su programa tomará una cadena, borrará todos los caracteres numéricos y devolverá una cadena con espacios y caracteres especiales ~#$%^&!@*():;"'.,?intactos.

def string_clean(s):
    res = ""
    for letra in s:
        if letra.isdecimal():
            res += ""
        else:
            res += letra
    return res
    
print(string_clean("123456789"))
print(string_clean("(E3at m2e2!!)"))
print(string_clean("! !"))
