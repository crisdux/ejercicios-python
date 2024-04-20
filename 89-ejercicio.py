# Dada una lista de strings, obtenga otra lista que contenga todos los caracteres de cada uno de los strings de la lista de         │
# │ entrada.

def chars_list(texts):
    texts = list("".join(texts))
    return texts
    
print(chars_list(['uno', 'dos', 'tres']))
print(chars_list(['', '', '']))
    