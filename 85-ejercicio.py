# Se te dará una cadena y tendrás que devolver la suma de todos los caracteres como un int. La función debería poder manejar todos los caracteres ASCII imprimibles.

# Ejemplos:

# uniTotal("a") == 97
# uniTotal("aaa") == 291

def uni_total(s):
    res = 0
    for i in s:
        res += ord(i)
    return res
    
print(uni_total("a"))
print(uni_total("aaa"))
