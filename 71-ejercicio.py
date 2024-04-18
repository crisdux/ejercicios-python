#  A partir de dos cadenas de texto compute el producto cartesiano letra a letra, dando como resultado un nuevo string completo.

def sprod_cart(text1, text2):
    res = ""
    for i in text1:
        for j in text2:
            res += f"{i}{j}"
            
    return res
print(sprod_cart("xy", "$#"))
print(sprod_cart("abc", "123"))
    