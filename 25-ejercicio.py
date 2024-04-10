# Un partido de la NBA dura 48 minutos (cuatro cuartos de 12 minutos). Los jugadores normalmente no juegan el juego completo, entrando y saliendo según sea necesario. Tu trabajo es extrapolar los puntos de un jugador por partido si jugó los 48 minutos completos.

# Escriba una función que tome dos argumentos, ppg (puntos por juego) y mpg (minutos por juego) y devuelva una extrapolación directa de ppg por 48 minutos redondeada a la décima más cercana. Devuelve 0 si es 0.

# Ejemplos:
# nba_extrap(12, 20) # 28.8
# nba_extrap(10, 10) # 48
# nba_extrap(5, 17) # 14.1
# nba_extrap(0, 0) # 0

def calcular_puntos(puntos, minutos_jugados):
    if puntos == 0 and minutos_jugados == 0:
        return 0
    return round((puntos * 48) / minutos_jugados, 1)
    
print(calcular_puntos(12,20))
print(calcular_puntos(10,10))
print(calcular_puntos(5,17))
print(calcular_puntos(0,0))