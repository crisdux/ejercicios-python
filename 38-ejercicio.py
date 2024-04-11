# # Elimina un signo de exclamación del final de una cadena. Para un kata principiante, puedes asumir que los datos de entrada son siempre una cadena, no es necesario verificarlo.

# "Hi!"     ---> "Hi"
# "Hi!!!"   ---> "Hi!!"
# "!Hi"     ---> "!Hi"
# "!Hi!"    ---> "!Hi"
# "Hi! Hi!" ---> "Hi! Hi"
# "Hi"      ---> "Hi"

def elimina_admiracion(cadena):
    if cadena[-1] != "!":
        return cadena
    lista = list(cadena)
    del lista[-1]
    return "".join(lista)
    
print(elimina_admiracion("Hi!"))
print(elimina_admiracion("Hi!!!" ))
print(elimina_admiracion("!Hi"))
print(elimina_admiracion("!Hi!"))
print(elimina_admiracion("Hi! Hi!" ))
print(elimina_admiracion("Hi" ))
