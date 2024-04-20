# ╭────────────────────────────────────────────────────── ENCONTRANDO ISOGRAMAS ──────────────────────────────────────────────────────╮
# │ Determine si una cadena de texto dada es un isograma, es decir, no se repite ninguna letra.                                       │
# │                                                                                                                                   │
# │ Notas:                                                                                                                            │
# │                                                                                                                                   │
# │  • No se puede utilizar la función count()                                                                                        │
# │  • Los guiones medios no cuentan como caracter repetido.

def is_isogram(text):
    text = text.lower()
    
    list_letras = []
    
    for letra in text:
        if letra == "-":
            continue
        if letra in list_letras:
            return False
        list_letras.append(letra)
    return True
            
            

print(is_isogram("circus"))
print(is_isogram("fantastical"))
print(is_isogram("symmetrical"))
print(is_isogram("lumberjacks"))