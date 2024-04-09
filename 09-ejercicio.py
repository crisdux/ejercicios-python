#  Dado un nombre, obtenga el nombre completo intercambiando nombre y apellidos.

def swap_name(full_name):
    nombre = full_name[:full_name.find(" ")].strip()
    apellido = full_name[full_name.find(" "):].strip()
    return f"{apellido} {nombre}"
    
print(swap_name("John McClane"))
print(swap_name("Charles Foster Kane"))
print(swap_name("Terminator T-800"))