#  Calcule la distancia hamming entre dos cadenas de texto dadas.                                                       │
# │                                                                                                                      │
# │ NOTAS:                                                                                                               │
# │                                                                                                                      │
# │  • Si las cadenas de texto tienen distinta longitud habrá que devolver -1.

def hamming(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()
    if len(text1) != len(text2):
        return -1
    list_index = []
    for index, value in enumerate(text1):
        if( value != text2[index]):
            list_index.append(index)
    return len(list_index)
    

print(hamming("0001010011101", "0000110010001"))                
print(hamming("abc", "acbd"))                
print(hamming("teclado", "techado"))
print(hamming("esperanza", "esmeralda"))
        