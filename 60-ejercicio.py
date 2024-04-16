# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def password_correcto():
    password = "maruchan"
    input_password = input("Escribe tu contraseña")
    while password != input_password:
        print("Password incorrecto")
        input_password = input("Escribe tu contraseña")
        
    print("Correcto! Bienvenido!")
    
print(password_correcto())
        