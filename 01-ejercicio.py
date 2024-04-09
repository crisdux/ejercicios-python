# Escriba un programa en Python que acepte el nombre y los apellidos de una persona y los devuelva en orden inverso separados por
# una coma. Utilice f-strings para implementarlo.

def switch_name(name, surname):
    return f"{surname}, {name}"

print(switch_name("Sergio", "Delgado Quintero"))
print(switch_name("Grace", "Hoper"))
print(switch_name("Guido", "Van Rossum"))