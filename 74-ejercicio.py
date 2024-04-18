# ╭──────────────────────────────────────────────────────── UN JUEGO AL TENIS ────────────────────────────────────────────────────────╮
# │ Escenario: Partido de Tenis. Dada una cadena de texto con letras A o B indicando si el jugador A ha ganado un punto o si el       │
# │ jugador B ha ganado un punto, haga un programa en Python que determine quién ha ganado el juego actual.                           │
# │                                                                                                                                   │
# │ Nota: Es obvio que el jugador que ha ganado el último punto del juego también ha ganado el juego, pero nos interesa irlo          │
# │ calculando de forma secuencial para prepararnos de cara a ejercicios más completos.

def tennis_game(points):
    count_a = points.count("A")
    count_b = points.count("B")
    
    if count_a > count_b:
        return "A"
    elif count_b > count_a:
        return "B"
        
print(tennis_game("ABAABA"))
print(tennis_game("BABABAABBB"))
print(tennis_game("AAABA"))
print(tennis_game("BBBAAAABABBAAA"))
    