# juan corre mucho, decide tomar 0.5L de agua por cada hora que corre.
# escribir una funcion que reciba la cantidad de horas corrida y regrese la cantidad de agua que debe
# tomar en litros redondeado hacia abajo.

import math

def calculo_agua(horas_corridas):
    return math.floor(.5 * horas_corridas)
    
print(calculo_agua(3))
print(calculo_agua(6.7))
print(calculo_agua(11.8))