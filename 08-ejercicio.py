#  Dada una cadena de texto, se pide eliminar el primer y el último caracter de dicha cadena de texto.

def strip1(text):
    string_a_lista = list(text)
    del string_a_lista[0]
    del string_a_lista[-1]
    return "".join(string_a_lista)
    
print(strip1("What can I do")) # hat can I d
print(strip1("Only when I sleep")) # nly when I slee
print(strip1("Runaway")) # unawa
print(strip1("Happiness")) # appines
    
    