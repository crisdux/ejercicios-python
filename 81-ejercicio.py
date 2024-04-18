# Dada una cadena de dígitos, debes reemplazar cualquier dígito inferior a 5 con '0' y cualquier dígito 5 o superior con '1'. Devuelve la cadena resultante.

def get_fake_binary(x):
    res = ""
    for i in x:
        if int(i) < 5:
            res += "0"
        else:
            res += "1"
            
    return res
    
print(get_fake_binary("45385593107843568"))