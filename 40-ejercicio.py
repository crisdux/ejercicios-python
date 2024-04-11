# Escriba una función llamada setAlarm// set_alarm/ set-alarm( setalarmsegún el idioma) que reciba dos parámetros. El primer parámetro, employedes verdadero siempre que esté empleado y el segundo parámetro, vacationes verdadero siempre que esté de vacaciones.

# La función debería volver a ser verdadera si está empleado y no de vacaciones (porque estas son las circunstancias en las que necesita configurar una alarma). De lo contrario, debería devolver falso. Ejemplos:

# employed | vacation 
# true     | true     => false
# true     | false    => true
# false    | true     => false
# false    | false    => false

def alarm(employe, vacation):
    if employe == True and vacation == False:
        return True
    else:
        return False
        
print(alarm(True, True))
print(alarm(True, False))
print(alarm(False, True))
print(alarm(False, False))