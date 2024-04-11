# Estabas acampando con tus amigos lejos de casa, pero cuando llega el momento de regresar, te das cuenta de que se te está acabando el combustible y que el surtidor más cercano está a 50kilómetros de distancia. Usted sabe que, en promedio, su automóvil recorre aproximadamente 25millas por galón. Quedan 2galones.

# Teniendo en cuenta estos factores, escribe una función que te indique si es posible llegar a la bomba o no.

# La función debe regresar true si es posible y false si no.

def km_a_millas(cantidad_km):
    return 0.62 * cantidad_km
    
def llegar_gasolinera(cantidad_galones, distancia_por_galon, distancia_a_recorrer):
    distancia_permitida = distancia_por_galon * cantidad_galones
    if distancia_permitida >= km_a_millas(distancia_a_recorrer):
        return True
    else:
        return False
print(llegar_gasolinera(2, 25, 50))
    
    