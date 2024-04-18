# El software de reconocimiento de caracteres se utiliza ampliamente para digitalizar textos impresos. De este modo, los textos se pueden editar, buscar y almacenar en un ordenador.

# Cuando los documentos (especialmente los bastante antiguos escritos con una máquina de escribir) se digitalizan, los software de reconocimiento de caracteres suelen cometer errores.

# Tu tarea es corregir los errores en el texto digitalizado. Sólo tienes que manejar los siguientes errores:

# S se malinterpreta como5
# Ose malinterpreta como0
# Ise malinterpreta como1
# Los casos de prueba contienen números sólo por error.

def correct(s):
    res = ""
    for i in s:
        if i == "5":
            res +="S"
        elif i == "0":
            res += "O"
        elif i == "1":
            res += "I"
        else:
            res += i
    return res

print(correct("L0ND0N"))