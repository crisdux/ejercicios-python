# Escriba un programa que acepte edad, peso, pulso y número de plaquetas de una persona y determine si cumple con los requisitos    │
# │ para donar sanger.

# https://www3.gobiernodecanarias.org/sanidad/ichh/donantes/requisitos.asp

def blood_donation(edad, peso, pulso, plaquetas):
    if (18<= edad <= 65) and peso > 50 and (50 <= pulso <=100) and plaquetas >= 150_000:
        return True
    else:
        return False
print(blood_donation(34,81,70,151000))
print(blood_donation(17,81,70,200000))
print(blood_donation(50,47,70,171000))
print(blood_donation(50,47,70,128000))
print(blood_donation(19,86,90,210000))
print(blood_donation(19,86,120,210000))
        